import argparse

parser = argparse.ArgumentParser(description='Calculates the needed bandwidth for your monitor cable.')

parser.add_argument("resolution_width", help="Width of your monitors resolution. eg 2560 in 2560x1440")
parser.add_argument("resolution_height",help="Height of your monitors resolution. eg 1440 in 2560x1440")
parser.add_argument("colour_depth", help="This is the bit rate of your monitor multiplied by 3. eg 8bit = 8x3= 24bits")
parser.add_argument("refresh_rate", help="This is how fast your monitor refreshes the screen per second normally 60hz can be higher 144Hz ect")
parser.add_argument("--overhead",default=1.2, help="For digital video transmission, there is typically overhead involved, often approximated to be around 20 percent. This accounts for blanking intervals, error correction, etc.")

args = vars(parser.parse_args())

bandwidth = int(args["resolution_width"]) * int(args["resolution_height"]) * int(args["colour_depth"]) * int(args["refresh_rate"]) * float(args["overhead"])
bandwidth = bandwidth / 1000000000
print("reso {} x {}".format(int(args["resolution_width"]), int(args["resolution_height"])))
print("colour depth: {}".format(int(args["colour_depth"])))
print("Refresh rate: {}".format(int(args["refresh_rate"])))
print("overhead: {}".format(float(args["overhead"])))

print(f"Calculated bandwidth: {bandwidth:.2f} Gbps")

