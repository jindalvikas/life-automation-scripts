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


# Below script is for Slabs import

f2=open('./slab_rider_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderSlabs.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >>f2,('rule "Mashreq Rider slab - '+row["riderCode"].strip()+', '+row["productCode"].strip()+', '+row["optionCode"].strip()+', '+row["currency"].strip()+'"' + '\n' +
		   '\t'.expandtabs(4) + 'when' + '\n' +
		        '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
		        	'\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "'+row["riderCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getProductCode() == "'+row["productCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "'+row["optionCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + '((riderRequest.getBasePlanSumAssured() >= '+row["minBaseSumAssured"].strip()+') && (riderRequest.getBasePlanSumAssured() <= '+row["maxBaseSumAssured"].strip()+')) &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getRuleId() == "slab" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getCurrency() == "'+row["currency"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq"' + '\n' +
		        '\t'.expandtabs(8) + ')' + '\n' +
		    '\t'.expandtabs(4) + 'then' + '\n' +
				'\t'.expandtabs(8) + 'RiderSlabResponse response = new RiderSlabResponse();' + '\n' +
		        '\t'.expandtabs(8) + 'response.setRiderCode(riderRequest.getRiderCode());' + '\n' +
		        '\t'.expandtabs(8) + 'response.setProductCode(riderRequest.getProductCode());' + '\n' +
	            '\t'.expandtabs(8) + 'response.setOptionCode(riderRequest.getOptionCode());' + '\n' +
		        '\t'.expandtabs(8) + 'response.setRiderSumAssured(Long.valueOf('+row["riderDefaultSumAssured"].strip()+'));' + '\n' +
		        '\t'.expandtabs(8) + 'response.setIsValid(true);' + '\n' +
	            '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
		'end\n')
        
f2.close()


# Below script is for interdependency import

f3=open('./interdependency_rider_mashreq.java', 'w+')

with open('./RiderInterdependency.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >> f3, ('rule "Mashreq Rider Interdependency - '+row["riderCode"].strip()+', '+row["productCode"].strip()+', '+row["optionCode"].strip()+'"' + '\n' +
		   '\t'.expandtabs(4) + 'when' + '\n' +
		        '\t'.expandtabs(8) + 'riderRequest:RiderRequest(' + '\n' +
		        	'\t'.expandtabs(12) + 'riderRequest.getRiderCode() == "'+row["riderCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getProductCode() == "'+row["productCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getOptionCode() == "'+row["optionCode"].strip()+'" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getRuleId() == "interDependentRiders" &&' + '\n' +
            		'\t'.expandtabs(12) + 'riderRequest.getBroker() == "mashreq"' + '\n' +
		        '\t'.expandtabs(8) + ')' + '\n' +
		    '\t'.expandtabs(4) + 'then' + '\n' +
		    	'\t'.expandtabs(8) + 'InterDependendRiderResponse response = new InterDependendRiderResponse();' + '\n' +
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
        		print >> f3, ('\t'.expandtabs(8) + 'includedRiders.add("'+includedRider+'");')

        if excludedRiderString is not None and len(excludedRiderString) != 0:
        	excludedRiders = [x.strip() for x in excludedRiderString.split(',')]
        	for excludedRider in excludedRiders:
        		print >> f3, ('\t'.expandtabs(8) + 'excludedRiders.add("'+excludedRider+'");')
		
		
		print >> f3, ('\t'.expandtabs(8) + 'response.setIncludedRiders(includedRiders);' + '\n' +
		        '\t'.expandtabs(8) + 'response.setExcludedRiders(excludedRiders);' + '\n' +
		        '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
		'end\n')
        
f3.close()

