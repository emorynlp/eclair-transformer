from eclair_transformer.eclair import ECLAIR
import json

helper = ECLAIR(task=2)
demo_dataset = \
{
    "train":[{
      "ResumeFileName": "49109.docx",
      "Qualification": "MBA, Keller Graduate School of Management : Master of Business Administration :  \r \t\t  Public Administration\t  2015 \r DeVry University - Decatur, GA, United States \r  \r B.S., DeVry University : Bachelor of Science :  \r Technical Management\t  2012 \r \t  DeVry University - Decatur, GA, United States",
      "SegregatedQualification": [
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 10,
            "Location": {
              "City": "Decatur",
              "State": "GA",
              "StateIsoCode": "US-GA",
              "Country": "United States",
              "CountryCode": {
                "IsoAlpha2": "US",
                "IsoAlpha3": "USA",
                "UNCode": "840"
              }
            }
          },
          "SubInstitution": {
            "Name": "Keller Graduate School of Management",
            "ConfidenceScore": 10,
            "Type": "School",
            "Location": {
              "City": "",
              "State": "",
              "StateIsoCode": "",
              "Country": "",
              "CountryCode": {
                "IsoAlpha2": "",
                "IsoAlpha3": "",
                "UNCode": ""
              }
            }
          },
          "Degree": {
            "DegreeName": "MBA, Master of Business Administration Public Administration",
            "NormalizeDegree": "Master of Business Administration",
            "Specialization": [
              "Public Administration"
            ],
            "ConfidenceScore": 10
          },
          "FormattedDegreePeriod": "2015",
          "StartDate": "",
          "EndDate": "31/12/2015",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        },
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 7,
            "Location": {
              "City": "",
              "State": "",
              "StateIsoCode": "",
              "Country": "",
              "CountryCode": {
                "IsoAlpha2": "",
                "IsoAlpha3": "",
                "UNCode": ""
              }
            }
          },
          "Degree": {
            "DegreeName": "B.S. , Bachelor of Science Technical Management",
            "NormalizeDegree": "Bachelor of Science",
            "Specialization": [
              "Technical Management"
            ],
            "ConfidenceScore": 8
          },
          "FormattedDegreePeriod": "2012",
          "StartDate": "",
          "EndDate": "31/12/2012",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        },
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 10,
            "Location": {
              "City": "Decatur",
              "State": "GA",
              "StateIsoCode": "US-GA",
              "Country": "United States",
              "CountryCode": {
                "IsoAlpha2": "US",
                "IsoAlpha3": "USA",
                "UNCode": "840"
              }
            }
          },
          "Degree": {
            "DegreeName": "",
            "NormalizeDegree": "",
            "Specialization": [],
            "ConfidenceScore": 0
          },
          "FormattedDegreePeriod": "",
          "StartDate": "",
          "EndDate": "",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        }
      ],
      "Certification": "",
      "SegregatedCertification": [],
      "Experience": "Staff management  \r Relationship and team building \r Team collaboration  \r  \r \t   \r  \r HIPAA compliance \r Time management \r Routine blood draws \r Patient safety  \r  \r Customer Service  \r  \r \tPhlebotomy Support Coordinator / Lab Assistant\tJul 2015 to Current \r Emory Healthcare-Winship Lab - Atlanta, GA \r Supervises and coordinates daily activities of staff including the registration, collection, and processing of laboratory specimens  \r Performs phlebotomy and collections for research patients \r Coordinates the flow of the office for a professional and friendly environment  \r Monitors operation and productivity, prepares work schedules, trains new employees, and oversees computer functions \r Orders and maintains an adequate inventory of commonly used supplies to ensure immediate availability, checks the expiration dates of stored items to ensure that the dates are not expired and takes appropriate action to remove any outdated items \r Evaluates new products as available and initiates implementation procedures as appropriate \r Coordinates the ordering and/or processing of patient specimens ensuring that  \r \t  each is properly collected, labeled, and transported to maintain the integrity of  \r \t  each specimen  \r Investigates and resolves problems and documents for monthly quality management reports  \r Follows up and resolves customer service complaints and documents appropriately \r Responsible for completing all data entry requirements, including but not limited to entry of the test order from or pulling order from database \r Manages standing orders that have not been resolved through standard operating procedures\t   \r Initiates intervention on unacceptable specimens as needed \r Participates and documents quality improvement activities as it relates to registration procedures, wait times, phlebotomy, processing and the transportation of specimens \r   \r \tPhlebotomist / Lab Assistant\tMar 1999 to Sep 2014 \r Quest Diagnostics - Decatur, GA \r Registered, collected, labeled, and processed patient specimens for testing in a timely manner including routine and advanced venipuncture along with other specimen collection as required \r Blood collection by venipuncture and capillary technique from patients of all age groups, urine drug screen collections, and urinalysis pediatric blood collections \r Worked with manager to formulate plan for professional development and trained new hire  \r Performed data entry, billing procedures, and verified insurance \r Maintained stock inventory",
      "SegregatedExperience": [
        {
          "Employer": {
            "EmployerName": "Emory Healthcare- Winship Lab",
            "FormattedName": "",
            "ConfidenceScore": 8
          },
          "JobProfile": {
            "Title": "Phlebotomy Support Coordinator/Lab Assistant",
            "FormattedName": "Medical Laboratory Assistant",
            "Alias": "assistant clinical researcher, assistant in biomedical laboratory, assistant in medical laboratory, biomedical laboratory assistant, biomedical laboratory research assistant, Lab assistant, lab associate, lab associate i\\/ii\\/iii, Laboratory Assistant, Medical lab assistant, medical laboratory research assistant",
            "RelatedSkills": [
              {
                "Skill": "Medical Evaluation",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Laboratory Automated Quality Control Systems",
                "ProficiencyLevel": "Proficient"
              },
              {
                "Skill": "Laboratory Testing",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Sample Preparation",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Perform Laboratory Tests",
                "ProficiencyLevel": "Proficient"
              }
            ],
            "ConfidenceScore": 10
          },
          "Location": {
            "City": "Atlanta",
            "State": "GA",
            "StateIsoCode": "US-GA",
            "Country": "USA",
            "CountryCode": {
              "IsoAlpha2": "US",
              "IsoAlpha3": "USA",
              "UNCode": "840"
            }
          },
          "JobPeriod": "Jul 2015 to Current",
          "FormattedJobPeriod": "07/2015 to till",
          "StartDate": "01/07/2015",
          "EndDate": "02/11/2020",
          "IsCurrentEmployer": "true",
          "JobDescription": "Supervises and coordinates daily activities of staff including the registration, collection, and processing of laboratory specimens \n Performs phlebotomy and collections for research patients \n Coordinates the flow of the office for a professional and friendly environment \n Monitors operation and productivity, prepares work schedules, trains new employees, and oversees computer functions \n Orders and maintains an adequate inventory of commonly used supplies to ensure immediate availability, checks the expiration dates of stored items to ensure that the dates are not expired and takes appropriate action to remove any outdated items \n Evaluates new products as available and initiates implementation procedures as appropriate \n Coordinates the ordering and/or processing of patient specimens ensuring that \n \t each is properly collected, labeled, and transported to maintain the integrity of \n \t each specimen \n Investigates and resolves problems and documents for monthly quality management reports \n Follows up and resolves customer service complaints and documents appropriately \n Responsible for completing all data entry requirements, including but not limited to entry of the test order from or pulling order from database \n Manages standing orders that have not been resolved through standard operating procedures\t \n Initiates intervention on unacceptable specimens as needed \n Participates and documents quality improvement activities as it relates to registration procedures, wait times, phlebotomy, processing and the transportation of specimens",
          "Projects": [
            {
              "UsedSkills": "",
              "ProjectName": "",
              "TeamSize": ""
            }
          ]
        },
        {
          "Employer": {
            "EmployerName": "Quest Diagnostics",
            "FormattedName": "",
            "ConfidenceScore": 8
          },
          "JobProfile": {
            "Title": "Phlebotomist/Lab Assistant",
            "FormattedName": "Phlebotomist",
            "Alias": "Clinical Phlebotomist, Phelbotomist, phlebotomist i, phlebotomist ii, Phlebotomy Practitioner, Phlebotomy Specialist, Phlebotomy Technician, Practitioner Of Phlebotomy, Specialist In Phlebotomy",
            "RelatedSkills": [
              {
                "Skill": "Phlebotomy",
                "ProficiencyLevel": "Proficient"
              },
              {
                "Skill": "Patient Education",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Health Care Analytics",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Lobotomy",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Venipuncture",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Techniques Of Blood Sampling",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Take Blood Samples",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Care Management",
                "ProficiencyLevel": "Moderate"
              }
            ],
            "ConfidenceScore": 10
          },
          "Location": {
            "City": "Decatur",
            "State": "GA",
            "StateIsoCode": "US-GA",
            "Country": "USA",
            "CountryCode": {
              "IsoAlpha2": "US",
              "IsoAlpha3": "USA",
              "UNCode": "840"
            }
          },
          "JobPeriod": "Mar 1999 to Sep 2014",
          "FormattedJobPeriod": "03/1999 to 09/2014",
          "StartDate": "01/03/1999",
          "EndDate": "30/09/2014",
          "IsCurrentEmployer": "false",
          "JobDescription": "Registered, collected, labeled, and processed patient specimens for testing in a timely manner including routine and advanced venipuncture along with other specimen collection as required \n Blood collection by venipuncture and capillary technique from patients of all age groups, urine drug screen collections, and urinalysis pediatric blood collections \n Worked with manager to formulate plan for professional development and trained new hire \n Performed data entry, billing procedures, and verified insurance \n Maintained stock inventory",
          "Projects": [
            {
              "UsedSkills": "",
              "ProjectName": "",
              "TeamSize": ""
            }
          ]
        }
      ],
      "CurrentEmployer": "Emory Healthcare- Winship Lab",
      "JobProfile": "Phlebotomy Support Coordinator/Lab Assistant",
      "WorkedPeriod": {
        "TotalExperienceInMonths": "252",
        "TotalExperienceInYear": "21.0",
        "TotalExperienceRange": "GREATER THAN 10 YEAR"
      },
      "JobDescription": "Perform a variety of research, data, and clerical duties of a routine and technical nature to support the conduct of clinical research. One year full time or part time equivalent experience in a healthcare setting (hospital, clinic, doctor's office) in a clinical role such as phlebotomist, medical assistant, patient care assistant, medical secretary, etc.  This position involves scheduling, specimen collection, laboratory processing, and shipping, and inventory management.",
      "Label": "YES"
    }],
    "eval": [
    {
      "ResumeFileName": "49109.docx",
      "Qualification": "MBA, Keller Graduate School of Management : Master of Business Administration :  \r \t\t  Public Administration\t  2015 \r DeVry University - Decatur, GA, United States \r  \r B.S., DeVry University : Bachelor of Science :  \r Technical Management\t  2012 \r \t  DeVry University - Decatur, GA, United States",
      "SegregatedQualification": [
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 10,
            "Location": {
              "City": "Decatur",
              "State": "GA",
              "StateIsoCode": "US-GA",
              "Country": "United States",
              "CountryCode": {
                "IsoAlpha2": "US",
                "IsoAlpha3": "USA",
                "UNCode": "840"
              }
            }
          },
          "SubInstitution": {
            "Name": "Keller Graduate School of Management",
            "ConfidenceScore": 10,
            "Type": "School",
            "Location": {
              "City": "",
              "State": "",
              "StateIsoCode": "",
              "Country": "",
              "CountryCode": {
                "IsoAlpha2": "",
                "IsoAlpha3": "",
                "UNCode": ""
              }
            }
          },
          "Degree": {
            "DegreeName": "MBA, Master of Business Administration Public Administration",
            "NormalizeDegree": "Master of Business Administration",
            "Specialization": [
              "Public Administration"
            ],
            "ConfidenceScore": 10
          },
          "FormattedDegreePeriod": "2015",
          "StartDate": "",
          "EndDate": "31/12/2015",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        },
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 7,
            "Location": {
              "City": "",
              "State": "",
              "StateIsoCode": "",
              "Country": "",
              "CountryCode": {
                "IsoAlpha2": "",
                "IsoAlpha3": "",
                "UNCode": ""
              }
            }
          },
          "Degree": {
            "DegreeName": "B.S. , Bachelor of Science Technical Management",
            "NormalizeDegree": "Bachelor of Science",
            "Specialization": [
              "Technical Management"
            ],
            "ConfidenceScore": 8
          },
          "FormattedDegreePeriod": "2012",
          "StartDate": "",
          "EndDate": "31/12/2012",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        },
        {
          "Institution": {
            "Name": "DeVry University",
            "Type": "University",
            "ConfidenceScore": 10,
            "Location": {
              "City": "Decatur",
              "State": "GA",
              "StateIsoCode": "US-GA",
              "Country": "United States",
              "CountryCode": {
                "IsoAlpha2": "US",
                "IsoAlpha3": "USA",
                "UNCode": "840"
              }
            }
          },
          "Degree": {
            "DegreeName": "",
            "NormalizeDegree": "",
            "Specialization": [],
            "ConfidenceScore": 0
          },
          "FormattedDegreePeriod": "",
          "StartDate": "",
          "EndDate": "",
          "Aggregate": {
            "Value": "",
            "MeasureType": ""
          }
        }
      ],
      "Certification": "",
      "SegregatedCertification": [],
      "Experience": "Staff management  \r Relationship and team building \r Team collaboration  \r  \r \t   \r  \r HIPAA compliance \r Time management \r Routine blood draws \r Patient safety  \r  \r Customer Service  \r  \r \tPhlebotomy Support Coordinator / Lab Assistant\tJul 2015 to Current \r Emory Healthcare-Winship Lab - Atlanta, GA \r Supervises and coordinates daily activities of staff including the registration, collection, and processing of laboratory specimens  \r Performs phlebotomy and collections for research patients \r Coordinates the flow of the office for a professional and friendly environment  \r Monitors operation and productivity, prepares work schedules, trains new employees, and oversees computer functions \r Orders and maintains an adequate inventory of commonly used supplies to ensure immediate availability, checks the expiration dates of stored items to ensure that the dates are not expired and takes appropriate action to remove any outdated items \r Evaluates new products as available and initiates implementation procedures as appropriate \r Coordinates the ordering and/or processing of patient specimens ensuring that  \r \t  each is properly collected, labeled, and transported to maintain the integrity of  \r \t  each specimen  \r Investigates and resolves problems and documents for monthly quality management reports  \r Follows up and resolves customer service complaints and documents appropriately \r Responsible for completing all data entry requirements, including but not limited to entry of the test order from or pulling order from database \r Manages standing orders that have not been resolved through standard operating procedures\t   \r Initiates intervention on unacceptable specimens as needed \r Participates and documents quality improvement activities as it relates to registration procedures, wait times, phlebotomy, processing and the transportation of specimens \r   \r \tPhlebotomist / Lab Assistant\tMar 1999 to Sep 2014 \r Quest Diagnostics - Decatur, GA \r Registered, collected, labeled, and processed patient specimens for testing in a timely manner including routine and advanced venipuncture along with other specimen collection as required \r Blood collection by venipuncture and capillary technique from patients of all age groups, urine drug screen collections, and urinalysis pediatric blood collections \r Worked with manager to formulate plan for professional development and trained new hire  \r Performed data entry, billing procedures, and verified insurance \r Maintained stock inventory",
      "SegregatedExperience": [
        {
          "Employer": {
            "EmployerName": "Emory Healthcare- Winship Lab",
            "FormattedName": "",
            "ConfidenceScore": 8
          },
          "JobProfile": {
            "Title": "Phlebotomy Support Coordinator/Lab Assistant",
            "FormattedName": "Medical Laboratory Assistant",
            "Alias": "assistant clinical researcher, assistant in biomedical laboratory, assistant in medical laboratory, biomedical laboratory assistant, biomedical laboratory research assistant, Lab assistant, lab associate, lab associate i\\/ii\\/iii, Laboratory Assistant, Medical lab assistant, medical laboratory research assistant",
            "RelatedSkills": [
              {
                "Skill": "Medical Evaluation",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Laboratory Automated Quality Control Systems",
                "ProficiencyLevel": "Proficient"
              },
              {
                "Skill": "Laboratory Testing",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Sample Preparation",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Perform Laboratory Tests",
                "ProficiencyLevel": "Proficient"
              }
            ],
            "ConfidenceScore": 10
          },
          "Location": {
            "City": "Atlanta",
            "State": "GA",
            "StateIsoCode": "US-GA",
            "Country": "USA",
            "CountryCode": {
              "IsoAlpha2": "US",
              "IsoAlpha3": "USA",
              "UNCode": "840"
            }
          },
          "JobPeriod": "Jul 2015 to Current",
          "FormattedJobPeriod": "07/2015 to till",
          "StartDate": "01/07/2015",
          "EndDate": "02/11/2020",
          "IsCurrentEmployer": "true",
          "JobDescription": "Supervises and coordinates daily activities of staff including the registration, collection, and processing of laboratory specimens \n Performs phlebotomy and collections for research patients \n Coordinates the flow of the office for a professional and friendly environment \n Monitors operation and productivity, prepares work schedules, trains new employees, and oversees computer functions \n Orders and maintains an adequate inventory of commonly used supplies to ensure immediate availability, checks the expiration dates of stored items to ensure that the dates are not expired and takes appropriate action to remove any outdated items \n Evaluates new products as available and initiates implementation procedures as appropriate \n Coordinates the ordering and/or processing of patient specimens ensuring that \n \t each is properly collected, labeled, and transported to maintain the integrity of \n \t each specimen \n Investigates and resolves problems and documents for monthly quality management reports \n Follows up and resolves customer service complaints and documents appropriately \n Responsible for completing all data entry requirements, including but not limited to entry of the test order from or pulling order from database \n Manages standing orders that have not been resolved through standard operating procedures\t \n Initiates intervention on unacceptable specimens as needed \n Participates and documents quality improvement activities as it relates to registration procedures, wait times, phlebotomy, processing and the transportation of specimens",
          "Projects": [
            {
              "UsedSkills": "",
              "ProjectName": "",
              "TeamSize": ""
            }
          ]
        },
        {
          "Employer": {
            "EmployerName": "Quest Diagnostics",
            "FormattedName": "",
            "ConfidenceScore": 8
          },
          "JobProfile": {
            "Title": "Phlebotomist/Lab Assistant",
            "FormattedName": "Phlebotomist",
            "Alias": "Clinical Phlebotomist, Phelbotomist, phlebotomist i, phlebotomist ii, Phlebotomy Practitioner, Phlebotomy Specialist, Phlebotomy Technician, Practitioner Of Phlebotomy, Specialist In Phlebotomy",
            "RelatedSkills": [
              {
                "Skill": "Phlebotomy",
                "ProficiencyLevel": "Proficient"
              },
              {
                "Skill": "Patient Education",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Health Care Analytics",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Lobotomy",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Venipuncture",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Techniques Of Blood Sampling",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Take Blood Samples",
                "ProficiencyLevel": "Moderate"
              },
              {
                "Skill": "Care Management",
                "ProficiencyLevel": "Moderate"
              }
            ],
            "ConfidenceScore": 10
          },
          "Location": {
            "City": "Decatur",
            "State": "GA",
            "StateIsoCode": "US-GA",
            "Country": "USA",
            "CountryCode": {
              "IsoAlpha2": "US",
              "IsoAlpha3": "USA",
              "UNCode": "840"
            }
          },
          "JobPeriod": "Mar 1999 to Sep 2014",
          "FormattedJobPeriod": "03/1999 to 09/2014",
          "StartDate": "01/03/1999",
          "EndDate": "30/09/2014",
          "IsCurrentEmployer": "false",
          "JobDescription": "Registered, collected, labeled, and processed patient specimens for testing in a timely manner including routine and advanced venipuncture along with other specimen collection as required \n Blood collection by venipuncture and capillary technique from patients of all age groups, urine drug screen collections, and urinalysis pediatric blood collections \n Worked with manager to formulate plan for professional development and trained new hire \n Performed data entry, billing procedures, and verified insurance \n Maintained stock inventory",
          "Projects": [
            {
              "UsedSkills": "",
              "ProjectName": "",
              "TeamSize": ""
            }
          ]
        }
      ],
      "CurrentEmployer": "Emory Healthcare- Winship Lab",
      "JobProfile": "Phlebotomy Support Coordinator/Lab Assistant",
      "WorkedPeriod": {
        "TotalExperienceInMonths": "252",
        "TotalExperienceInYear": "21.0",
        "TotalExperienceRange": "GREATER THAN 10 YEAR"
      },
      "JobDescription": "Perform a variety of research, data, and clerical duties of a routine and technical nature to support the conduct of clinical research. One year full time or part time equivalent experience in a healthcare setting (hospital, clinic, doctor's office) in a clinical role such as phlebotomist, medical assistant, patient care assistant, medical secretary, etc.  This position involves scheduling, specimen collection, laboratory processing, and shipping, and inventory management.",
      "Label": "YES"
    }
    ]
}
helper.train(demo_dataset)
crc=helper.decode(demo_dataset["train"][0])
print(json.dumps(crc, indent=2))
helper.save("demo_output/demo_save_model")