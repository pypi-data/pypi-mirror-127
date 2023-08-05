from simulacra.theory import TheoryModel
import numpy.random as random
import astropy.units as u
import astropy.coordinates as coord
import astropy.time as at
import telfit
import logging
import numpy as np



class TelFitModel(TheoryModel):
    def __init__(self,lambmin,lambmax,loc='APO',humidity=50.0,temperature=300*u.Kelvin,pressure=1.0e6*u.Pa,wave_padding=10*u.Angstrom):
        self._name = 'tellurics'
        self.wave_padding = wave_padding
        self.lambmin = lambmin
        self.lambmax = lambmax
        # assert that all of these parameters that are arrays
        # are the same length
        # or they are just a scalar
        self.epoches     = None
        self.temperature = temperature
        self.pressure    = pressure
        self.humidity    = humidity

        # dlamb = 1e-2 * u.Angstrom
        # self.wave = np.arange(lambmin.to(u.Angstrom).value,lambmax.to(u.Angstrom).value,step=dlamb.to(u.Angstrom).value) * u.Angstrom

        self.loc = loc

    def check_shape_type(self,value,unit=None):
        if isinstance(value, u.Quantity):
            if value.unit.physical_type in unit.physical_type:
                if self.epoches:
                    if value.shape[0] == self.epoches:
                        return value
                    elif len(value.shape) == 0:
                        return value * np.ones(self.epoches)
                    else:
                        logging.warn('input not the correct size {}'.format(self.epoches))
                else:
                    if len(value.shape) == 0:
                        return value
                    else:
                        self.epoches = value.shape[0]
                        return value
        logging.warn('type or physical type are not correct')
        return None

    def temperature():
        doc = "The temperature property."
        def fget(self):
            return self._temperature
        def fset(self, value):
            out = self.check_shape_type(value,unit=u.Kelvin)
            if out is not None:
                self._temperature = out
            else:
                print('temperature left as default {}'.format(self.temperature))

        def fdel(self):
            del self._temperature
        return locals()
    temperature = property(**temperature())

    def pressure():
        doc = "The pressure property."
        def fget(self):
            return self._pressure
        def fset(self,value):
            out = self.check_shape_type(value,unit=u.Pa)
            if out is not None:
                self._pressure = out
            else:
                print('pressure left as default {}'.format(self.pressure))

        def fdel(self):
            del self._pressure
        return locals()
    pressure = property(**pressure())

    def humidity():
        doc = "The humidity property."
        def fget(self):
            return self._humidity
        def fset(self, value):
            if isinstance(value, float):
                self._humidity = value * np.ones(self.epoches)
            elif isinstance(value, np.ndarray):
                if value.shape[0] == self.epoches:
                    self._humidity = value
                else:
                    logging.warn('ndarray incorrect shape')
            else:
                logging.warn('incorrect type: must be float or ndarray')

        def fdel(self):
            del self._humidity
        return locals()
    humidity = property(**humidity())

    def check_property(self,property,value):
        if len(property.shape) == 0:
            return property * np.ones(value)
        elif property.shape[0] < value:
            logging.warn('epoches larger than the set temperatures\npadding with last element')
            temp = property
            return np.concatenate((temp,temp[-1] * np.ones(value - temp.shape[0])))
        elif property.shape[0] > value:
            logging.warn('epoches smaller than the set temperatures\ntruncating elements')
            return property[:value]
        else:
            return property

    def epoches():
        doc = "The epoches property."
        def fget(self):
            return self._epoches
        def fset(self,value):
            self._epoches = value
            try:
                self.temperature = self.check_property(self.temperature,value)
            except AttributeError:
                pass
            try:
                self.pressure = self.check_property(self.pressure,value)
            except AttributeError:
                pass
            try:
                self.humidity = self.check_property(self.humidity,value)
            except AttributeError:
                pass
        def fdel(self):
            del self._epoches
        return locals()
    epoches = property(**epoches())

    def generate_transmission(self,star,detector,obs_times,exp_times):
        times = at.Time([obs_times[i] + exp_times[i]/2 for i in range(len(obs_times))])
        telescope_frame = coord.AltAz(obstime=obs_times,location=detector.loc)
        secz = np.array(star.target.transform_to(telescope_frame).secz)
        # singlerun = self.epoches is None
        if self.epoches != obs_times.shape[0]:
            logging.warning('tellurics epoches not the same as obs times\nresetting...')
            self.epoches = obs_times.shape[0]

        modeler = telfit.Modeler(debug=True)
        flux = []
        wave = []
        # print(self.lambmin.to(u.cm),self.lambmax.to(u.cm)
        for i,time in enumerate(obs_times):

            angle = np.arccos(1./secz[i]) * 180 * u.deg/np.pi
            print('humidity: {}\n'.format(self.humidity[i]),
                'pressure: {}\n'.format(self.pressure[i].to(u.hPa).value),
                'temperature: {}\n'.format(self.temperature[i].to(u.Kelvin).value),
                'lat: {}\n'.format(self.loc.lat.to(u.degree).value),
                'elevation: {}\n'.format(self.loc.height.to(u.km).value),
                'freqmin(cm-1): {}\n'.format(1.0/(self.lambmax.to(u.cm).value)),
                'freqmax(cm-1): {}\n'.format(1.0/(self.lambmin.to(u.cm).value)),
                'angle: {}\n'.format(angle.to(u.deg).value))

            model = modeler.MakeModel(humidity=self.humidity[i],
                         pressure=float(self.pressure[i].to(u.hPa).value),
                         temperature=float(self.temperature[i].to(u.Kelvin).value),
                         lat=float(self.loc.lat.to(u.degree).value),
                         alt=float(self.loc.height.to(u.km).value),
                         lowfreq=float(1.0/self.lambmax.to(u.cm).value),
                         highfreq=float(1.0/self.lambmin.to(u.cm).value),
                         angle=float(angle.to(u.deg).value))


            ns   = len(model.x)
            # if singlerun:
            #     for time in obs_times:
            #         flux.append(model.y)
            #         wave.append(model.x * u.nm)
            #     return flux, wave
            print(ns)
            flux.append(model.y)
            wave.append(model.x * u.nm)

        # flux = flux.reshape(self.epoches,ns)
        # wave = wave.reshape(self.epoches,ns)
        return flux, wave

    @TheoryModel.lambmin.setter
    def lambmin(self,lambmin):
        self._lambmin = lambmin - self.wave_padding

    @TheoryModel.lambmax.setter
    def lambmax(self,lambmax):
        self._lambmax = lambmax + self.wave_padding
