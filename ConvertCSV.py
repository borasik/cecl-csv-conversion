# ! /usr/bin/python
import pandas as pd
import sys, getopt



def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
   except getopt.GetoptError:
      print ('ConvertCSV.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('ConvertCSV.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   try:
      df = pd.read_csv(inputfile, sep='|', header=None)
      df.rename(columns={0: 'borrowerShortName',
                   2: 'rimNumber', 3: 'rimType', 4: 'accountType', 5: 'accountNumber', 6: 'branchNumber',
                   8: 'commitmentBalance', 9: 'undisbursedBalanceOnLoan',
                   10: 'undisbursedBalanceOnCommitments', 11: 'originalContractAmount', 12: 'accountStatus', 13: 'participationFlag', 
                   14: 'participationBalance', 15: 'sbaGuaranteedFlag', 16: 'sbaGuaranteedAgencyCode', 17: 'sbaGuaranteedPercent',
                   18: 'usGuaranteedFlag', 19: 'usGuaranteedCode', 20: 'usGuaranteedPercent', 21: 'currentEffectiveRate',
                   22: 'rateIndex', 23: 'spreadOverIndex', 24: 'daysPastDue', 25: 'daysTomaturity',
                   26: 'internalBorrowerRiskRating', 27: 'daysFromRiskRating', 28: '30DayPastDueCounter', 29: '60DayPastDueCounter',
                   30: '90DayPastDueCounter', 31: '120DayPastDueCounter', 32: '150DayPastDueCounter', 33: '180DayPastDueCounter',
                   34: 'daysFromNonAccrualFlag', 35: 'collateralId', 36: 'propertyType', 37: 'loanTypeForHmdactReporting',
                   38: 'occupancyType', 39: 'hmdaOccupancy', 40: 'primaryCollateralValue', 41: 'daysFromPrimaryCollateralValue',
                   42: 'renegotiatedDebtIndicator', 43: 'grossChargedOffBalance', 44: 'activeBalance', 45: 'nonAccruingBalance',
                   46: 'classCode', 47: 'purposeCode', 48: 'callCode', 50: 'naicsCode',
                   52: 'naicsSector', 54: 'daysPrincipalDaysPaidThrough', 55: 'daysInterestDaysPaidThrough',
                   56: 'daysToNextPrincipalDue', 57: 'daysToNextInterestDue', 58: 'extractMonth', 59: 'extractYear',
                   62: 'totalAmountofCommitments', 63: 'undisbursedExposure', 64: 'participationIndicator', 65: 'weightedAverageFacilityRiskRating',
                   66: 'facilityRiskRating1', 67: 'facilityRiskRatingPercent1', 68: 'facilityRiskRating2', 69: 'facilityRiskRatingPercent2',
                   70: 'facilityRiskRating3', 71: 'facilityRiskRatingPercent3', 72: 'facilityRiskRating4', 73: 'facilityRiskRatingPercent4',
                   74: 'calculatedLoanToValue', 75: 'writedownLtd', 76: 'writedownMtd', 77: 'chargeOffLtd',
                   78: 'chargeOffMtd', 79: 'recoveryLtd', 80: 'recoveryMtd', 81: 'recoveredInterestLtd',
                   82: 'recoveredInterestMtd', 83: 'parentCommitmentType1', 84: 'parentCommitmentNumber1', 85: 'parentCommitmentType2',
                   86: 'parentCommitmentNumber2', 87: 'subaccountType', 88: 'valuesFromCreWorksheet', 89: 'censusTract',
                   90: 'msa', 91: 'daysToNextRate'
                   }, inplace=True)
      df.to_csv(outputfile, index=False,
          columns=['borrowerShortName','rimNumber', 'rimType','accountType', 'accountNumber',  'branchNumber',
                   'commitmentBalance', 'undisbursedBalanceOnLoan', 'undisbursedBalanceOnCommitments', 'originalContractAmount',
                   'accountStatus', 'participationFlag','participationBalance', 'sbaGuaranteedFlag', 'sbaGuaranteedAgencyCode', 
                   'sbaGuaranteedPercent','usGuaranteedFlag','usGuaranteedCode','usGuaranteedPercent', 'currentEffectiveRate',
                   'rateIndex', 'spreadOverIndex', 'daysPastDue', 'daysTomaturity','internalBorrowerRiskRating', 'daysFromRiskRating', 
                   '30DayPastDueCounter', '60DayPastDueCounter','90DayPastDueCounter', '120DayPastDueCounter',  '150DayPastDueCounter',
                   '180DayPastDueCounter','daysFromNonAccrualFlag', 'collateralId', 'propertyType', 'loanTypeForHmdactReporting',
                   'occupancyType', 'hmdaOccupancy', 'primaryCollateralValue', 'daysFromPrimaryCollateralValue',
                   'renegotiatedDebtIndicator', 'grossChargedOffBalance', 'activeBalance', 'nonAccruingBalance',
                   'classCode', 'purposeCode', 'callCode', 'naicsCode', 'naicsSector', 'daysPrincipalDaysPaidThrough',
                   'daysInterestDaysPaidThrough', 'daysToNextPrincipalDue', 'daysToNextInterestDue', 'extractMonth', 'extractYear',
                   'totalAmountofCommitments', 'undisbursedExposure', 'participationIndicator', 'weightedAverageFacilityRiskRating',
                   'facilityRiskRating1', 'facilityRiskRatingPercent1', 'facilityRiskRating2', 'facilityRiskRatingPercent2',
                   'facilityRiskRating3', 'facilityRiskRatingPercent3', 'facilityRiskRating4', 'facilityRiskRatingPercent4',
                   'calculatedLoanToValue', 'writedownLtd', 'writedownMtd', 'chargeOffLtd', 'chargeOffMtd', 'recoveryLtd', 'recoveryMtd', 
                   'recoveredInterestLtd','recoveredInterestMtd', 'parentCommitmentType1', 'parentCommitmentNumber1','parentCommitmentType2',
                   'parentCommitmentNumber2', 'subaccountType', 'valuesFromCreWorksheet', 'censusTract', 'msa', 'daysToNextRate'], sep=',')
   except:
      print("Unexpected error:", sys.exc_info()[0])
      raise 


if __name__ == "__main__":
   main(sys.argv[1:])
