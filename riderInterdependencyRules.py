import csv

def generateRiderInterdependencyRules(file_path, output_file, broker):
    # Below script is for interdependency import

    f1 = open(output_file, 'w+')

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        s8 = ' ' * 8
        s12 = ' ' * 12

        ruleNameText = 'rule "{0} Rider Interdependency - {1}, {2}, {3}"\n'

        whenRuleText = """    when
        riderRequest:RiderRequest(
            riderRequest.getRiderCode() == "{0}" &&
            riderRequest.getProductCode() == "{1}" &&
            riderRequest.getOptionCode() == "{2}" &&
            riderRequest.getRuleId() == "interDependentRiders" &&
            riderRequest.getBroker() == "{3}"
        )
"""

        thenResponseText = """    then
        InterDependendRiderResponse response = new InterDependendRiderResponse();
        response.setRiderCode(riderRequest.getRiderCode());
        response.setProductCode(riderRequest.getProductCode());
        response.setOptionCode(riderRequest.getOptionCode());
        ArrayList<String> includedRiders = new ArrayList<>();
        ArrayList<String> excludedRiders = new ArrayList<>();{}
        response.setIncludedRiders(includedRiders);
        response.setExcludedRiders(excludedRiders);
        rulesResponse.setRuleResponse(response);
end
"""

        for row in csv_reader:
            row = {k: v.strip() for k, v in row.items()}
            ruleName = ruleNameText.format(broker.capitalize(), row["riderCode"], row["productCode"], row["optionCode"])
            whenRule = whenRuleText.format(row["riderCode"], row["productCode"], row["optionCode"], broker)

            includedRiderString = row["includedRiders"]
            excludedRiderString = row["excludedRiders"]

            thenResponseRidersData = ""
            if includedRiderString is not None and len(includedRiderString) != 0:
                includedRiders = [x.strip() for x in includedRiderString.split(',')]
                for includedRider in includedRiders:
                    thenResponseRidersData += '\n' + s8 + 'includedRiders.add("' + includedRider + '");'

            if excludedRiderString is not None and len(excludedRiderString) != 0:
                excludedRiders = [x.strip() for x in excludedRiderString.split(',')]
                for excludedRider in excludedRiders:
                    thenResponseRidersData += '\n' + s8 + 'excludedRiders.add("' + excludedRider + '");'

            thenResponse = thenResponseText.format(thenResponseRidersData)
            print((ruleName + whenRule + thenResponse), file=f1)

    f1.close()
