import ReadPix4flow
from time import sleep
import sys

def main():
    test = ReadPix4flow.ReadPix4flow(tty="COM4")
    p = 0
    with open("sample.txt",'w') as f:
        f.write("%+15s" % "time_usec" + "%+15s" % "flow_x" + "%+15s" % "flow_y" + "%+15s" % "flow_comp_m_x" + "%+15s" % "flow_comp_m_y")
        f.write("\n")
    with open("samplerad.txt",'w') as f:
        f.write("%+15s" % "time_usec_rad" + "%+15s" % "integ_time_us" + "%+15s" % "integ_x" + "%+15s" % "integ_y" + "%+15s" % "integ_xgyro" + "%+15s" % "integ_ygyro")
        f.write("\n")
    test.start()
    while p <= 10:
        try:
            sleep(1)
            p = p + 1
        except KeyboardInterrupt:
            test.stop()
            sys.exit()
    test.writeflow()
    test.writeflowrad()
    test.stop()
    sys.exit()

main()
