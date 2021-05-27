import csv

def generateRiderSlabRules(file_path, output_file, broker):
    # Below script is for Slabs import

    f1 = open(output_file, 'w+')

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        s12 = ' ' * 12

        ruleNameText = 'rule "{0} Rider slab - {1}, {2}, {3}, {4}, BP_SA FROM {5} TO {6}"\n'

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

            ruleName = ruleNameText.format(broker.capitalize(), row["productCode"], row["optionCode"], row["currency"], row["riderCode"], row["minBaseSumAssured"], row["maxBaseSumAssured"])

            whenRule = whenRuleText.format(
                row["riderCode"], row["productCode"], row["optionCode"], row["minBaseSumAssured"], row["maxBaseSumAssured"],
                row["currency"], broker
            )

            thenResponse = thenResponseText.format(row["riderDefaultSumAssured"].strip())

            # PYTHON 3
            print((ruleName + whenRule + thenResponse), file=f1)
            # PYTHON 2
            # print >> f1, (ruleName + whenRule + thenResponse)

    f1.close()
