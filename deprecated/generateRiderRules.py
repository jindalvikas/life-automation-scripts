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

# Below script is for Slabs import

f2 = open('./slab_rider_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderSlabs.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >> f2, ('rule "Mashreq Rider slab - ' + row["riderCode"].strip() + ', ' + row[
            "productCode"].strip() + ', ' + row["optionCode"].strip() + ', ' + row["currency"].strip() + '"' + '\n' +
                      '\t'.expandtabs(4) + 'when' + '\n' +
                      '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "' + row[
                          "riderCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getProductCode() == "' + row[
                          "productCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "' + row[
                          "optionCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + '((riderRequest.getBasePlanSumAssured() >= ' + row[
                          "minBaseSumAssured"].strip() + ') && (riderRequest.getBasePlanSumAssured() <= ' + row[
                          "maxBaseSumAssured"].strip() + ')) &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getRuleId() == "slab" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getCurrency() == "' + row[
                          "currency"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq"' + '\n' +
                      '\t'.expandtabs(8) + ')' + '\n' +
                      '\t'.expandtabs(4) + 'then' + '\n' +
                      '\t'.expandtabs(8) + 'RiderSlabResponse response = new RiderSlabResponse();' + '\n' +
                      '\t'.expandtabs(8) + 'response.setRiderCode(riderRequest.getRiderCode());' + '\n' +
                      '\t'.expandtabs(8) + 'response.setProductCode(riderRequest.getProductCode());' + '\n' +
                      '\t'.expandtabs(8) + 'response.setOptionCode(riderRequest.getOptionCode());' + '\n' +
                      '\t'.expandtabs(8) + 'response.setRiderSumAssured(Long.valueOf(' + row[
                          "riderDefaultSumAssured"].strip() + '));' + '\n' +
                      '\t'.expandtabs(8) + 'response.setIsValid(true);' + '\n' +
                      '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
                      'end\n')

f2.close()

# Below script is for interdependency import

f3 = open('./interdependency_rider_mashreq.java', 'w+')

with open('./RiderInterdependency.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >> f3, ('rule "Mashreq Rider Interdependency - ' + row["riderCode"].strip() + ', ' + row[
            "productCode"].strip() + ', ' + row["optionCode"].strip() + '"' + '\n' +
                      '\t'.expandtabs(4) + 'when' + '\n' +
                      '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "' + row[
                          "riderCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getProductCode() == "' + row[
                          "productCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "' + row[
                          "optionCode"].strip() + '" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getRuleId() == "interDependentRiders" &&' + '\n' +
                      '\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq"' + '\n' +
                      '\t'.expandtabs(8) + ')' + '\n' +
                      '\t'.expandtabs(4) + 'then' + '\n' +
                      '\t'.expandtabs(
                          8) + 'InterDependendRiderResponse response = new InterDependendRiderResponse();' + '\n' +
                      '\t'.expandtabs(8) + 'response.setRiderCode(riderRequest.getRiderCode());' + '\n' +
                      '\t'.expandtabs(8) + 'response.setProductCode(riderRequest.getProductCode());' + '\n' +
                      '\t'.expandtabs(8) + 'response.setOptionCode(riderRequest.getOptionCode());' + '\n' +
                      '\t'.expandtabs(8) + 'ArrayList<String> includedRiders = new ArrayList<>();' + '\n' +
                      '\t'.expandtabs(8) + 'ArrayList<String> excludedRiders = new ArrayList<>();')

        includedRiderString = row["includedRiders"].strip()
        excludedRiderString = row["excludedRiders"].strip()

        if includedRiderString is not None and len(includedRiderString) != 0:
            includedRiders = [x.strip() for x in includedRiderString.split(',')]
            for includedRider in includedRiders:
                print >> f3, ('\t'.expandtabs(8) + 'includedRiders.add("' + includedRider + '");')

        if excludedRiderString is not None and len(excludedRiderString) != 0:
            excludedRiders = [x.strip() for x in excludedRiderString.split(',')]
            for excludedRider in excludedRiders:
                print >> f3, ('\t'.expandtabs(8) + 'excludedRiders.add("' + excludedRider + '");')

        print >> f3, ('\t'.expandtabs(8) + 'response.setIncludedRiders(includedRiders);' + '\n' +
                      '\t'.expandtabs(8) + 'response.setExcludedRiders(excludedRiders);' + '\n' +
                      '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
                      'end\n')

f3.close()
