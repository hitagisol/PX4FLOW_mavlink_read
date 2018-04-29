from threading import Thread
import serial
from Pix4flowDriver import Pix4flowDriver


class ReadPix4flow(Thread):
    def __init__(self,tty='COM4',baud=9600):
        self.terminate = False
        self.handler = None
        self.tty = tty
        self.baud = baud
        self.time_usec = []
        self.flow_x = []
        self.flow_y = []
        self.flow_comp_m_x = []
        self.flow_comp_m_y = []
        self.time_usec_rad = []
        self.integration_time_us = []
        self.integrated_x = []
        self.integrated_y = []
        self.integrated_xgyro = []
        self.integrated_ygyro = []

        Thread.__init__(self)

    def commHandler(self):
        handler = None
        try:
            if handler is None:
                handler = serial.Serial(self.tty,self.baud,timeout = 3)
            return handler
        except serial.SerialException:
            handler = None
            return handler

    def run(self):
        self.handler = self.commHandler()
        while self.terminate == False:
            try:

                pix4 = Pix4flowDriver(self.handler,)
                pix4.refresh_opticalflow()
                pix4.refresh_opticalflowrad()
                self.time_usec.append(pix4.return_time_usec())
                self.flow_x.append(pix4.return_flowx())
                self.flow_y.append(pix4.return_flowy())
                self.flow_comp_m_x.append(pix4.return_flow_comp_m_x())
                self.flow_comp_m_y.append(pix4.return_flow_comp_m_y())

                self.time_usec_rad.append(pix4.return_time_usec_rad())
                self.integration_time_us.append(pix4.return_integration_time_us())
                self.integrated_x.append(pix4.return_integrated_x())
                self.integrated_y.append(pix4.return_integrated_y())
                self.integrated_xgyro.append(pix4.return_integrated_xgyro())
                self.integrated_ygyro.append(pix4.return_integrated_ygyro())

            except OSError:
                self.terminate == True
        if self.terminate == True:
            if (self.handler is not None):
                self.handler.close()
                self.handler = None

    def writeflow(self, filename="sample.txt"):
        with open(filename, 'a') as f:
            for i in range(0, len(self.time_usec)):
                f.write("%+15d" % self.time_usec[i] + "%+15d" % self.flow_x[i] + "%+15d" % self.flow_y[i] + "%+15.3e" %
                        self.flow_comp_m_x[i] + "%15.3e" % self.flow_comp_m_y[i] + "\n")
            del self.time_usec[:]
            del self.flow_x[:]
            del self.flow_y[:]
            del self.flow_comp_m_x[:]
            del self.flow_comp_m_y[:]

    def writeflowrad(self, filename="samplerad.txt"):
        with open(filename, 'a') as f:
            for i in range(0, len(self.time_usec_rad)):
                f.write("%+15d" % self.time_usec_rad[i] + "%+15d" % self.integration_time_us[i] + "%+15.3e" %
                        self.integrated_x[i] + "%+15.3e" % self.integrated_y[i] + "%+15.3e" % self.integrated_xgyro[
                            i] + "%+15.3e" % self.integrated_ygyro[i] + "\n")
            del self.time_usec_rad[:]
            del self.integration_time_us[:]
            del self.integrated_x[:]
            del self.integrated_y[:]
            del self.integrated_xgyro[:]
            del self.integrated_ygyro[:]

    def stop(self):
        self.terminate = True
        print "Programme terminated"
