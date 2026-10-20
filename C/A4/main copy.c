#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <stdbool.h>

#include "course.h"
#include "student.h"

#define LINE_LEN 50
#define COURSE_ID_LEN 5
#define MAX_COURSES_TAKEN 5

void insertStudentNode (struct StudentListNode *firstNode, struct StudentListNode *newNode)
{
printf("pre insertstud");

	struct StudentListNode *currNode = firstNode;
	struct StudentListNode *prevNode  = NULL;

	while (currNode != NULL)
	{
		prevNode = currNode;
		currNode = currNode->next;
	}

	if (prevNode == NULL)
	{
		studFirstNode = newNode;
	}
	else
	{
		prevNode->next = newNode;
	}
printf("post insertstud");

}

struct StudentListNode *getStudentNode (struct StudentListNode *firstNode, int id)
{
	struct StudentListNode *currNode = firstNode;

	while (currNode != NULL)
	{
		if (currNode->data.id == id){
			return currNode;
		}
		else{
			currNode = currNode->next;
		}
	}
	return NULL;
}

void insertCourseNode (struct CourseListNode *firstNode, struct CourseListNode *newNode)
{
printf("pre insertcourse");
	struct CourseListNode *currNode = firstNode;
	struct CourseListNode *prevNode  = NULL;

	if(firstNode == NULL){
		courseFirstNode = newNode;
printf("post insertcourse, new");
		return;
	}

	while(true){
		if(currNode == NULL){
			prevNode->next = newNode;
			break;
		}
		else if(strcmp(currNode->data.id,newNode->data.id) > 0){
			struct CourseListNode *after = currNode->next;
			prevNode->next = newNode;
			newNode->next = after;
			break;
		}
		prevNode = currNode;
		currNode = currNode->next;
	}
	
//	return firstNode;

	// struct CourseListNode *currNode = firstNode;
	// struct CourseListNode *prevNode  = NULL;

	// while ((currNode != NULL) && (strcmp(currNode->data.id,newNode) < 0))
	// {
	// 	prevNode = currNode;
	// 	currNode = currNode->next;
	// }

	// if (prevNode == NULL)
	// {
	// 	courseFirstNode = newNode;
	// }
	// else
	// {
	// 	struct CourseListNode *after = currNode->next;
	// 	prevNode->next = newNode;
	// 	newNode->next = after;
	// }
	printf("post insertcourse");
}

struct CourseListNode *getCourse(struct CourseListNode *firstNode, char courseName[])
{
	struct CourseListNode *currNode = firstNode;

	while (currNode != NULL)
	{
		if (strcmp(currNode->data.name, courseName) == 0){
			return currNode;
		}
		else{
			currNode = currNode->next;
		}
	}
	return NULL;
}

void insertStudName(int *studIds, int id, int enrollmentNum){
	int i = 0;
	while(true){
		if(studIds[i] == 0){
			studIds[i] = id;
			break;
		}
		else if(studIds[i] > id){
			for(int j = enrollmentNum-1; j >= i; j--){
				studIds[j+1] = studIds[j];
			}
			studIds[i] = id;
			break;
		}
		i++;
	}
}

void readInputFrom(char* fileName)
{
	printf("hi");
	FILE* studInfo = fopen(fileName, "r");
	
	int iStud = -1;

	int courseCount = -1;

	char line[LINE_LEN];

	int currStudId = 0;
	// currStud.id = 0;
	// currStud.name[0] = '\0';
	// currStud.courses = NULL;

	while(fscanf(studInfo, "%s", line) != EOF){
		// struct Student currStud;
		if(strcmp(line, "Student") == 0){
			//int currID = 0;
			//char currStud[LINE_LEN];
			char currStudName[LINE_LEN];

			iStud++;
			fscanf(studInfo, "%d", &currStudId);
			fscanf(studInfo, " %s", currStudName);

			struct StudentListNode *currNode = (struct StudentListNode *)calloc (1, sizeof (struct StudentListNode));

			currNode->data.id = currStudId;
			strcpy(currNode->data.name,currStudName);
			currNode->data.courses = (char**)calloc(MAX_COURSES_TAKEN, sizeof(char*));

			printf("outside");
			insertStudentNode (studFirstNode, currNode);

			courseCount = -1;
			/*
			studentNames[iStud] = (char*)malloc(LINE_LEN*sizeof(char));
			strcpy(studentNames[iStud],currStud);
			
				
			studentIDs[iStud] = currID;
			studentTakesCourses[iStud] = (char**)calloc(MAX_COURSES_TAKEN, sizeof(char*));
			courseCount = -1;
*/
		}
		else{
			// struct Course currCourse;
			// //char courseCode[COURSE_ID_LEN];
			courseCount++;
			// currCourse.name = line;
			// currCourse.enrollmentNum = 0;
			// currCourse.students = NULL;
			// fscanf(studInfo, "%s",currCourse.id);

			char courseCode[COURSE_ID_LEN];
			//courseCount++;
			fscanf(studInfo, "%s",courseCode);
			struct CourseListNode *node = getCourse(courseFirstNode, line);
			if(node == NULL){
				struct CourseListNode *currNode = (struct CourseListNode*)malloc(sizeof(struct CourseListNode));
				strcpy(currNode->data.id, courseCode);
				//char courseCode[COURSE_ID_LEN];
				//courseCount++;

				strcpy(currNode->data.name, line);
				currNode->data.enrollmentNum = 1;
				currNode->data.students = (int*)calloc(MAX_STUDENT_NUM, sizeof(int));
				currNode->data.students[0] = currStudId;
				currNode->next = NULL;

				insertCourseNode (courseFirstNode, currNode);
				
			}
			else{
				insertStudName(node->data.students,currStudId,node->data.enrollmentNum++);
				// node->data.enrollmentNum++;
				//node->data.students[node->data.enrollmentNum++] = currStudId;
				


				// for(int i = 0; i < MAX_STUDENT_NUM; i++){
				// 	if(node->data.students[i] == NULL){
				// 		//node->data.students[i] == (id of current student)
				// 		break;
				// 	}
				// }
			}

			struct StudentListNode* studNode = getStudentNode (studFirstNode, currStudId);

			if (studNode != NULL)
			{
				studNode->data.courses[courseCount] = (char*)malloc(COURSE_ID_LEN*sizeof(char));
				strcpy(studNode->data.courses[courseCount], courseCode);
			}





			
			//add course to current student's course list


			// bool found = false;
			// for(int i = 0; i < MAX_COURSE_NUM; i++){
			// 	if(courseIDs[i] == NULL){
			// 		courseIDs[i] = (char*)malloc(COURSE_ID_LEN*sizeof(char));
			// 		strcpy(courseIDs[i], courseCode);
					
			// 		courseNames[i] = (char*)malloc(LINE_LEN*sizeof(char));
			// 		strcpy(courseNames[i], line);

			// 		found = true;
			// 	}	
			// 	else if(strcmp(courseCode, courseIDs[i]) == 0){
			// 		found = true;
			// 	}
				
			// 	if(found){
			// 		if(courseTakenByStudents[i] == NULL){
			// 			courseTakenByStudents[i] = (int*)calloc(MAX_STUDENT_NUM, sizeof(int));				
			// 		}
			// 		courseTakenByStudents[i][courseEnrollment[i]] = studentIDs[iStud];
			// 		courseEnrollment[i]++;
					
			// 		studentTakesCourses[iStud][courseCount] = (char*)malloc(COURSE_ID_LEN*sizeof(char));
			// 		strcpy(studentTakesCourses[iStud][courseCount], courseCode);
			// 		break;
			// 	}
			// }

		}
	}
}

void writeOutputTo(char* fileName)
{
	FILE* courseInfo = fopen(fileName, "w");

	struct CourseListNode *currNode = courseFirstNode;
	while(currNode != NULL){
		fprintf(courseInfo, "Course %s %s %d\n", currNode->data.id, currNode->data.name, currNode->data.enrollmentNum);
		int i = 0;
		while(currNode->data.students[i] != 0){
			struct StudentListNode *student = getStudentNode (studFirstNode, currNode->data.students[i]);
			fprintf(courseInfo, "%d %s\n", student->data.id, student->data.name);
			i++;
		}
		currNode = currNode->next;
	}
	
	// int i = 0;
	// while(courseIDs[i] != NULL){
	// 	fprintf(courseInfo, "Course %s %s %d\n", courseIDs[i], courseNames[i], courseEnrollment[i]);
		
	// 	int j = 0;
	// 	while(courseTakenByStudents[i][j] != 0){
	// 		int k = 0;
	// 		while(studentIDs[k] != courseTakenByStudents[i][j]){
	// 			k++;
	// 		}
	// 		fprintf(courseInfo, "%d %s\n", studentIDs[k], studentNames[k]);
	// 		j++;
	// 	}
	// 	i++;
	// }
	fclose(courseInfo);
}
 
void cleanup()
{
	void freeStud(struct StudentListNode *firstNode){

		struct StudentListNode *currNode = firstNode;
		struct StudentListNode *nextNode  = NULL;

		while (currNode != NULL)
		{
			nextNode = currNode->next;
			int i = 0;
			while (currNode->data.courses[i] != NULL && i < MAX_COURSES_TAKEN) {
				free(currNode->data.courses[i++]);
			}

			free (currNode->data.courses);
			free (currNode);

			currNode = nextNode;
		}
	}

	void freeCourse(struct CourseListNode *firstNode){
		struct CourseListNode *currNode = firstNode;
		struct CourseListNode *nextNode  = NULL;

		while (currNode != NULL)
		{
			nextNode = currNode->next;

			free (currNode->data.students);
			free (currNode);

			currNode = nextNode;
		}
	}

	freeStud(studFirstNode);
	freeCourse(courseFirstNode);


	// void freeElem(char* arr[], int size){
	// 	int i = 0;
	// 	while(arr[i] != NULL && i < size){
	// 		free(arr[i]);
	// 		i++;
	// 	}
	// }
	
	// void freeElemInt(int* arr[], int size){
	// 	int i = 0;
	// 	while(arr[i] != NULL && i < size){
	// 		free(arr[i]);
	// 		i++;
	// 	}
	// }

	// freeElem(courseIDs, MAX_COURSE_NUM);
	// freeElem(courseNames, MAX_COURSE_NUM);
	// freeElem(studentNames, MAX_STUDENT_NUM);
	// freeElemInt(courseTakenByStudents, MAX_COURSE_NUM);

	// for (int i = 0; i < MAX_STUDENT_NUM; i++){
	// 	if(studentTakesCourses[i] == NULL){
	// 		break;
	// 	}

	// 	int j = 0;
	//  	while (studentTakesCourses[i][j] != NULL && i < MAX_COURSES_TAKEN) {
	// 		free(studentTakesCourses[i][j]);
	// 		j++;
	// 	}

	// 	free (studentTakesCourses[i]);
	// }
}


int main(int argc, char** argv)
{
printf("hello");
  char* inputFile = "studentInfo.txt";
  char* outputFile = "courseInfo.txt";
  if(argc == 3) {
    inputFile = argv[1];
    outputFile = argv[2];
  }
  readInputFrom(inputFile);
  writeOutputTo(outputFile);
  cleanup();
  return 0;
}  

