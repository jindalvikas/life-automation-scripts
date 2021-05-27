import csv
import argparse

# Initialize parser
parser = argparse.ArgumentParser()
# EXAMPLE
# python2 generateRiderValidationRules.py -f /Users/vaibhavsawant/Desktop/RiderValidationRules.csv -o ./life_rider_validations_mashreq.java -b turtlemint

# Adding optional argument
parser.add_argument("-f", "--file_path", help="Input File Path")
parser.add_argument("-o", "--output_file", help="Output File Path")
parser.add_argument("-b", "--broker", help="Broker")

# Read arguments from command line
args = parser.parse_args()

if args.file_path:
    print("file_path: % s" % args.file_path)

if args.output_file:
    print("output_file: % s" % args.output_file)

if args.broker:
    print("broker: % s" % args.broker)

# Below script is for Slabs import

f1 = open(args.output_file, 'w+')

with open(args.file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    s12 = ' ' * 12

    ruleNameText = 'rule "{0} Rider slab - {1}, {2}, {3}, {4}"\n'

    whenRuleText = """    when
        riderRequest:RiderRequest(
            riderRequest.getRiderCode() == "{0}" &&
            riderRequest.getProductCode() == "{1}" &&
            riderRequest.getOptionCode() == "{2}" &&
            ((riderRequest.getBasePlanSumAssured() >= {3}) && (riderRequest.getBasePlanSumAssured() <=  {4})) &&
            riderRequest.getRuleId() == "slab" &&
            riderRequest.getCurrency() == "{5}" &&
            riderRequest.getBroker() == "{6}"
        )
"""

    thenResponseText = """    then
        RiderSlabResponse response = new RiderSlabResponse();
        response.setRiderCode(riderRequest.getRiderCode());
        response.setProductCode(riderRequest.getProductCode());
        response.setOptionCode(riderRequest.getOptionCode());
        response.setRiderSumAssured(Long.valueOf({0}));
        response.setIsValid(true);
        rulesResponse.setRuleResponse(response);
end
"""


    for row in csv_reader:
        row = {k: v.strip() for k, v in row.items()}

        ruleName = ruleNameText.format(args.broker.capitalize(), row["productCode"], row["optionCode"], row["currency"], row["riderCode"])

        whenRule = whenRuleText.format(
            row["riderCode"], row["productCode"], row["optionCode"], row["minBaseSumAssured"], row["maxBaseSumAssured"],
            row["currency"], args.broker
        )

        thenResponse = thenResponseText.format(row["riderDefaultSumAssured"].strip())

        # PYTHON 3
        print((ruleName + whenRule + thenResponse), file=f1)
        # PYTHON 2
        # print >> f1, (ruleName + whenRule + thenResponse)

f1.close()
