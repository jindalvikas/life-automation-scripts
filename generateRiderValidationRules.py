import csv

# Below is the script for Validation rules

f1=open('./life_rider_validations_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderValidationRules_mashreq.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >>f1,('rule "Mashreq Rider Validation Rule - '+row["riderCode"].strip()+', '+row["productCode"].strip()+', '+row["optionCode"].strip()+', '+row["currency"].strip()+'"' + '\n' +
		   '\t'.expandtabs(4) + 'when' + '\n' +
		        '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "'+row["riderCode"].strip()+'" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getProductCode() == "'+row["productCode"].strip()+'" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "'+row["optionCode"].strip()+'" &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getEntryAge() >= '+row["minEntryAge"].strip()+') && (riderRequest.getEntryAge() <= '+row["maxEntryAge"].strip()+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getMaturityAge() >= '+row["minMaturityAge"].strip()+') && (riderRequest.getMaturityAge() <= '+row["maxMaturityAge"].strip()+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderPolicyTerm() >= '+row["MinPolicyTerm"].strip()+') && (riderRequest.getRiderPolicyTerm() <= '+row["MaxPolicyTerm"].strip()+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderPremiumPaymentTerm() >= '+row["MinPremiumPaymentTerm"].strip()+') && (riderRequest.getRiderPremiumPaymentTerm() <= '+row["maxPremiumPaymentTerm"].strip()+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderSumAssured() >= '+row["MinSumAssured"].strip()+') && (riderRequest.getRiderSumAssured() <= '+row["MaxSumAssured"].strip()+')) &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderPolicyTerm() <= riderRequest.getBasePlanPolicyTerm() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderPremiumPaymentTerm() <= riderRequest.getBasePlanPremiumPaymentTerm() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderSumAssured() <= riderRequest.getBasePlanSumAssured() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getCurrency() == "'+row["currency"].strip()+'" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRuleId() == "validateRiders"' + '\n' +
		        '\t'.expandtabs(8) + ')' + '\n' +
		    '\t'.expandtabs(4) + 'then' + '\n' +
		        '\t'.expandtabs(8) + 'ValidRiderResponse validRiderResponse = new ValidRiderResponse();' + '\n' +
		        '\t'.expandtabs(8) + 'validRiderResponse.setRiderCode(riderRequest.getRiderCode());' + '\n' +
		        '\t'.expandtabs(8) + 'validRiderResponse.setProductCode(riderRequest.getProductCode());' + '\n' +
		        '\t'.expandtabs(8) + 'validRiderResponse.setOptionCode(riderRequest.getOptionCode());' + '\n' +
		        '\t'.expandtabs(8) + 'validRiderResponse.setValid(true);' + '\n' +
		        '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(validRiderResponse);' + '\n' +
		'end\n')
        
f1.close()

