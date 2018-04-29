import Mavlinkprotocol

class Pix4flowDriver:
    def __init__(self, handler, flowid='\x64', flowradid='\x6A'):
        self.handler = handler
        self.optical_flow_handler = Mavlinkprotocol.Mavlinkprotocol(self.handler, flowid)
        self.optical_flow_rad_handler = Mavlinkprotocol.Mavlinkprotocol(self.handler, flowradid)

    def refresh_opticalflow(self):
        self.optical_flow_handler.refresh()

    def return_time_usec(self):
        return self.optical_flow_handler.getvalue('Q', 0, 8)[0]

    def return_flowx(self):
        return self.optical_flow_handler.getvalue('h',20,22)[0]

    def return_flowy(self):
        return self.optical_flow_handler.getvalue('h',22,24)[0]

    def return_flow_comp_m_x(self):
        return self.optical_flow_handler.getvalue('f',8,12)[0]

    def return_flow_comp_m_y(self):
        return self.optical_flow_handler.getvalue('f',12,16)[0]

    def return_ground_distance(self):
        return self.optical_flow_handler.getvalue('f',17,20)[0]

    def refresh_opticalflowrad(self):
        self.optical_flow_rad_handler.refresh()

    def return_time_usec_rad(self):
        return self.optical_flow_rad_handler.getvalue('Q',0,8)[0]

    def return_integration_time_us(self):
        return self.optical_flow_rad_handler.getvalue('I',8,12)[0]

    def return_integrated_x(self):
        return self.optical_flow_rad_handler.getvalue('f',12,16)[0]

    def return_integrated_y(self):
        return self.optical_flow_rad_handler.getvalue('f',16,20)[0]

    def return_integrated_xgyro(self):
        return self.optical_flow_rad_handler.getvalue('f',20,24)[0]

    def return_integrated_ygyro(self):
        return self.optical_flow_rad_handler.getvalue('f',24,28)[0]

    def return_integrated_zgyro(self):
        return self.optical_flow_rad_handler.getvalue('f',28,32)[0]

    def return_time_delta_distance_us(self):
        return self.optical_flow_rad_handler.getvalue('I',32,36)[0]

    def return_distance(self):
        return self.optical_flow_rad_handler.getvalue('f',36,40)[0]