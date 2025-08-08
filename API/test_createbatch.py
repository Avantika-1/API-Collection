import allure
import pytest
import requests

@pytest.mark.sanity
@allure.description("Positive scenario: Create batch")
def test_create_batch():
    base_url = "api-testing.testaonline.com/"
    endpoint = "/api/createbatch"
    url = base_url + endpoint

    headers = {
        "x-auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFiaGlqZWV0QHJhZGlhbnRpbmZvbmV0LmNvbSIsImlwIjoiMTQuOTkuMTU1LjY2IiwiaWF0IjoxNzUxNDMyOTk3LCJleHAiOjE3NTE1MTkzOTd9.p3NU_p6QfZXgrYKpdNKfjPcSrQcqxjIYSzwvviHiS-I",
        "content-type": "application/json"
    }

    payload = {
        "batchSize": "200",
        "batchId": "APIbatch",
        "startDate": "01/07/2025",
        "endDate": "10/07/2025",
        "accessorId": "67483e240003919c6dbf5e1b",
        "assessorFeePerCandidate": "100",
        "assignAssessorProctor": "true",
        "batchEndDate": "16/06/2025",
        "batchMode": "online",
        "batchStartDate": "16/06/2025",
        "endTime": "05:55PM",
        "examCenterId": "67beac3f30b552125b2df6cf",
        "jobRole": "673d84a1567847b4f2041153",
        "proctoring": {
            "imageProctor": {
                "imageProctorStatus": "true",
                "imageProctoringTime": 1
            },
            "browserExit": {
                "browserExitAlert": "true",
                "noOfBrowserExit": 7
            },
            "capturingImageStatus": "true",
            "faceDetection": "false",
            "faceRecognition": "false",
            "identityProofStatus": "true",
            "isAutoLogout": "false",
            "videoScreensharingProctoringStatus": "true",
            "videoStream": {
                "videoStreaming": "true",
                "videoDuration": 5,
                "videoInterval": 1
            },
            "wrongLogin": {
                "wrongLoginStatus": "true",
                "noOfWrongLogin": 3
            }
        },
        "questionPaper": {
            "suffleQuestion": True,
            "optionRandom": "false",
            "markForReview": True,
            "questionNavigation": True,
            "assesmentStatus": True,
            "chooseInstructions": "682ef670cb1bac04b8c547b1",
            "examLanguageConduct": "false",
            "isMultiJobRole": False,
            "level": "5",
            "paginationStatus": True,
            "passingPercentage": "30",
            "primaryLanguage": "english",
            "qpCode": "673d84a1567847b4f2041153",
            "questionSet": "1",
            "questionType": "objective",
            "sectionTable": [
                {
                    "sectionName": "theory",
                    "sectionOrder": 1,
                    "examDuration": "30",
                    "isSelected": True
                }
            ],
            "version": "3"
        },
        "schemeId": "673ae2a21d9f795a1f756974",
        "startTime": "12:00AM",
        "subSchemeId": "673ae2ae1d9f795a1f756986"
    }

    response = requests.post(url=url, headers=headers, json=payload)

    print("Response Text:", response.text)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
