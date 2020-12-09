import csv

# Below is the script for Validation rules

f1 = open('./life_rider_validations_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderValidationRules_mashreq.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    s12 = ' ' * 12

    ruleNameText = 'rule "Mashreq Rider Validation Rule - {0}, {1}, {2}, {3}"\n'

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
            riderRequest.getBroker() == "mashreq" &&
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

        ruleName = ruleNameText.format(row["riderCode"], row["productCode"], row["optionCode"], row["currency"])

        whenRule = whenRuleText.format(
            row["riderCode"], row["productCode"], row["optionCode"], row["minEntryAge"], row["maxEntryAge"],
            row["minMaturityAge"], row["maxMaturityAge"], row["MinPolicyTerm"], row["MaxPolicyTerm"],
            row["MinPremiumPaymentTerm"], row["maxPremiumPaymentTerm"], row["MinSumAssured"], row["MaxSumAssured"],
            riderSALessThanCheck, row["currency"]
        )

        print >> f1, (ruleName + whenRule + thenResponse)

f1.close()
