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
	struct StudentListNode *currNode = firstNode;
	struct StudentListNode *prevNode = NULL;

	while(currNode != NULL && currNode->data.id < newNode->data.id)
	{
		prevNode = currNode;
		currNode = currNode->next;
	}

	if (prevNode == NULL)
	{
		struct StudentListNode *after = firstNode;
		studFirstNode = newNode;
		newNode->next = after;
	}
	else if (currNode == NULL){
		prevNode->next = newNode;
	}
	else
	{
		prevNode->next = newNode;
		newNode->next = currNode;
	}
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
	struct CourseListNode *currNode = firstNode;
	struct CourseListNode *prevNode  = NULL;

	while(currNode != NULL && strcmp(currNode->data.id,newNode->data.id) < 0)
	{
		prevNode = currNode;
		currNode = currNode->next;
	}

	if (prevNode == NULL)
	{
		struct CourseListNode *after = firstNode;
		courseFirstNode = newNode;
		newNode->next = after;
	}
	else if (currNode == NULL){
		prevNode->next = newNode;
	}
	else
	{
		prevNode->next = newNode;
		newNode->next = currNode;
	}
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
	FILE* studInfo = fopen(fileName, "r");
	
	if (studInfo == NULL){
		printf("Couldn't open input file\n");
		return false;
	}
	
	int courseCount = -1;
	int currStudId = 0;

	char line[LINE_LEN];

	while(fscanf(studInfo, "%s", line) != EOF){
		if(strcmp(line, "Student") == 0){
			char currStudName[LINE_LEN];

			fscanf(studInfo, "%d", &currStudId);
			fscanf(studInfo, " %s", currStudName);

			struct StudentListNode *currNode = (struct StudentListNode *)calloc (1, sizeof (struct StudentListNode));

			currNode->data.id = currStudId;
			strcpy(currNode->data.name,currStudName);
			currNode->data.courses = (char**)calloc(MAX_COURSES_TAKEN, sizeof(char*));

			insertStudentNode (studFirstNode, currNode);

			courseCount = -1;
		}
		else{
			courseCount++;
			char courseCode[COURSE_ID_LEN];

			fscanf(studInfo, "%s",courseCode);
			struct CourseListNode *node = getCourse(courseFirstNode, line);
			if(node == NULL){
				struct CourseListNode *currNode = (struct CourseListNode*)malloc(sizeof(struct CourseListNode));
				strcpy(currNode->data.id, courseCode);

				strcpy(currNode->data.name, line);
				currNode->data.enrollmentNum = 1;
				currNode->data.students = (int*)calloc(MAX_STUDENT_NUM, sizeof(int));
				currNode->data.students[0] = currStudId;
				currNode->next = NULL;

				insertCourseNode (courseFirstNode, currNode);				
			}
			else{
				insertStudName(node->data.students,currStudId,node->data.enrollmentNum++);
			}

			struct StudentListNode* studNode = getStudentNode (studFirstNode, currStudId);

			if (studNode != NULL)
			{
				studNode->data.courses[courseCount] = (char*)malloc(COURSE_ID_LEN*sizeof(char));
				strcpy(studNode->data.courses[courseCount], courseCode);
			}
		}
	}
	return true;
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
}

int main(int argc, char** argv)
{
  char* inputFile = NULL;
  char* outputFile = NULL;
  inputFile = argv[1];
  outputFile = argv[2];
  readInputFrom(inputFile)
  writeOutputTo(outputFile);
  cleanup();
  return 0;
}