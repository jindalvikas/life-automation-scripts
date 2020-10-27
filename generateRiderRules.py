import csv
f1=open('./life_rider_validations_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderValidationRules_mashreq.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >>f1,('rule "Rider Validation Rule - '+row["riderCode"]+', '+row["productCode"]+', '+row["optionCode"]+', '+row["currency"]+'"' + '\n' +
		   '\t'.expandtabs(4) + 'when' + '\n' +
		        '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "'+row["riderCode"]+'" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getProductCode() == "'+row["productCode"]+'" &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "'+row["optionCode"]+'" &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getEntryAge() >= '+row["minEntryAge"]+') && (riderRequest.getEntryAge() <= '+row["maxEntryAge"]+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getMaturityAge() >= '+row["minMaturityAge"]+') && (riderRequest.getMaturityAge() <= '+row["maxMaturityAge"]+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderPolicyTerm() >= '+row["MinPolicyTerm"]+') && (riderRequest.getRiderPolicyTerm() <= '+row["MaxPolicyTerm"]+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderPremiumPaymentTerm() >= '+row["MinPremiumPaymentTerm"]+') && (riderRequest.getRiderPremiumPaymentTerm() <= '+row["maxPremiumPaymentTerm"]+')) &&' + '\n' +
		            '\t'.expandtabs(12) + '((riderRequest.getRiderSumAssured() >= '+row["MinSumAssured"]+') && (riderRequest.getRiderSumAssured() <= '+row["MaxSumAssured"]+')) &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderPolicyTerm() <= riderRequest.getBasePlanPolicyTerm() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderPremiumPaymentTerm() <= riderRequest.getBasePlanPremiumPaymentTerm() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getRiderSumAssured() <= riderRequest.getBasePlanSumAssured() &&' + '\n' +
		            '\t'.expandtabs(12) + 'riderRequest.getCurrency() == "'+row["currency"]+'" &&' + '\n' +
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

f2=open('./slab_rider_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderSlabs.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >>f2,('rule "Mashreq Rider slab - '+row["riderCode"]+', '+row["productCode"]+', '+row["optionCode"]+', '+row["currency"]+'"' + '\n' +
		   '\t'.expandtabs(4) + 'when' + '\n' +
		        '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
		        	'\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "'+row["riderCode"]+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getProductCode() == "'+row["productCode"]+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "'+row["optionCode"]+'" &&' + '\n' +
            		'\t'.expandtabs(12) + '((riderRequest.getBasePlanSumAssured() >= '+row["minBaseSumAssured"]+') && (riderRequest.getBasePlanSumAssured() <= '+row["maxBaseSumAssured"]+')) &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getRuleId() == "slab" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getCurrency() == "'+row["currency"]+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq"' + '\n' +
		        '\t'.expandtabs(8) + ')' + '\n' +
		    '\t'.expandtabs(4) + 'then' + '\n' +
				'\t'.expandtabs(8) + 'RiderSlabResponse response = new RiderSlabResponse();' + '\n' +
		        '\t'.expandtabs(8) + 'response.setRiderCode(riderRequest.getRiderCode());' + '\n' +
		        '\t'.expandtabs(8) + 'response.setProductCode(riderRequest.getProductCode());' + '\n' +
	            '\t'.expandtabs(8) + 'response.setOptionCode(riderRequest.getOptionCode());' + '\n' +
		        '\t'.expandtabs(8) + 'response.setRiderSumAssured(Long.valueOf('+row["riderDefaultSumAssured"]+'));' + '\n' +
		        '\t'.expandtabs(8) + 'response.setIsValid(true);' + '\n' +
	            '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
		'end\n')
        
f2.close()