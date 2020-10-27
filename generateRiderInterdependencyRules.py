import csv

# Below script is for interdependency import

f1=open('./interdependency_rider_mashreq.java', 'w+')

with open('./RiderInterdependency.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print >> f1, ('rule "Mashreq Rider Interdependency - '+row["riderCode"].strip()+', '+row["productCode"].strip()+', '+row["optionCode"].strip()+'"' + '\n' +
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
        		print >> f1, ('\t'.expandtabs(8) + 'includedRiders.add("'+includedRider+'");')

        if excludedRiderString is not None and len(excludedRiderString) != 0:
        	excludedRiders = [x.strip() for x in excludedRiderString.split(',')]
        	for excludedRider in excludedRiders:
        		print >> f1, ('\t'.expandtabs(8) + 'excludedRiders.add("'+excludedRider+'");')
		
		
		print >> f1, ('\t'.expandtabs(8) + 'response.setIncludedRiders(includedRiders);' + '\n' +
		        '\t'.expandtabs(8) + 'response.setExcludedRiders(excludedRiders);' + '\n' +
		        '\t'.expandtabs(8) + 'rulesResponse.setRuleResponse(response);' + '\n' +
		'end\n')
        
f1.close()

