import csv


# Below script is for Slabs import

f1=open('./slab_rider_mashreq.java', 'w+')

with open('/Users/vikas/Desktop/RiderSlabs.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >>f1,('rule "Mashreq Rider slab - '+row["riderCode"].strip()+', '+row["productCode"].strip()+', '+row["optionCode"].strip()+', '+row["currency"].strip()+'"' + '\n' +
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
        
f1.close()
