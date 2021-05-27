import csv

def generateValidationRules(file_path, output_file, broker):
# Below is the script for Validation rules

    f1 = open(output_file, 'w+')

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        s12 = ' ' * 12

        ruleNameText = 'rule "{0} Rider Validation Rule - {1}, {2}, {3}, {4}"\n'

        whenRuleText = """    when
        riderRequest:RiderRequest(
            riderRequest.getRiderCode() == "{0}" &&
            riderRequest.getProductCode() == "{1}" &&
            riderRequest.getOptionCode() == "{2}" &&
            ((riderRequest.getEntryAge() >= {3}) && (riderRequest.getEntryAge() <= {4})) &&
            ((riderRequest.getMaturityAge() >= {5}) && (riderRequest.getMaturityAge() <= {6})) &&
            ((riderRequest.getRiderPolicyTerm() >= {7}) && (riderRequest.getRiderPolicyTerm() <= {8})) &&
            ((riderRequest.getRiderPremiumPaymentTerm() >= {9}) && (riderRequest.getRiderPremiumPaymentTerm() <= {10})) &&
            ((riderRequest.getRiderSumAssured() >= {11}) && (riderRequest.getRiderSumAssured() <= {12})) &&
            riderRequest.getRiderPolicyTerm() <= riderRequest.getBasePlanPolicyTerm() &&
            riderRequest.getRiderPremiumPaymentTerm() <= riderRequest.getBasePlanPremiumPaymentTerm() &&{13}
            riderRequest.getCurrency() == "{14}" &&
            riderRequest.getBroker() == "{15}" &&
            riderRequest.getRuleId() == "validateRiders"
        )
"""

        thenResponse = """    then
        ValidRiderResponse validRiderResponse = new ValidRiderResponse();
        validRiderResponse.setRiderCode(riderRequest.getRiderCode());
        validRiderResponse.setProductCode(riderRequest.getProductCode());
        validRiderResponse.setOptionCode(riderRequest.getOptionCode());
        validRiderResponse.setValid(true);
        rulesResponse.setRuleResponse(validRiderResponse);
end
"""

        for row in csv_reader:
            row = {k: v.strip() for k, v in row.items()}

            if row["PlanType"] == 'Term':
                riderSALessThanCheck = '\n' + s12 + 'riderRequest.getRiderSumAssured() <= riderRequest.getBasePlanSumAssured() &&'
            else:
                riderSALessThanCheck = ""

            ruleName = ruleNameText.format(broker.capitalize(), row["productCode"], row["optionCode"], row["currency"], row["riderCode"])

            whenRule = whenRuleText.format(
                row["riderCode"], row["productCode"], row["optionCode"], row["minEntryAge"], row["maxEntryAge"],
                row["minMaturityAge"], row["maxMaturityAge"], row["MinPolicyTerm"], row["MaxPolicyTerm"],
                row["MinPremiumPaymentTerm"], row["maxPremiumPaymentTerm"], row["MinSumAssured"], row["MaxSumAssured"],
                riderSALessThanCheck, row["currency"], broker
            )

            # PYTHON 3
            print((ruleName + whenRule + thenResponse), file=f1)
            # PYTHON 2
            # print >> f1, (ruleName + whenRule + thenResponse)

    f1.close()
