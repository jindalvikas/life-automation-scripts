import argparse
from riderValidationRules import generateValidationRules
from riderSlabRules import generateRiderSlabRules
from riderInterdependencyRules import generateRiderInterdependencyRules

# Initialize parser
parser = argparse.ArgumentParser()
# EXAMPLE
# python lifeMain.py -g validationRules -f /Users/vaibhavsawant/Desktop/RiderValidationRules.csv -o ./life_rider_validations_turtlemint.java -b turtlemint

generateChoices = ['validationRules', 'slabRules', 'interdependencyRules']

# Adding optional argument
parser.add_argument("-g", "--generate", action='store', choices=generateChoices, help="Rules Action")
parser.add_argument("-f", "--file_path", help="Input File Path")
parser.add_argument("-o", "--output_file", help="Output File Path")
parser.add_argument("-b", "--broker", help="Broker")

# Read arguments from command line
args = parser.parse_args()

if args.generate:
    print("broker: % s" % args.generate)

if args.file_path:
    print("file_path: % s" % args.file_path)

if args.output_file:
    print("output_file: % s" % args.output_file)

if args.broker:
    print("broker: % s" % args.broker)

if args.generate == "validationRules":
    generateValidationRules(args.file_path, args.output_file, args.broker)
elif args.generate == "slabRules":
    generateRiderSlabRules(args.file_path, args.output_file, args.broker)
elif args.generate == "interdependencyRules":
    generateRiderInterdependencyRules(args.file_path, args.output_file, args.broker)

