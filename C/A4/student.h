#ifndef STUDENT_H
#define STUDENT_H

#define MAX_STUDENT_NUM 100
#define NAME_LEN 100

struct Student{
	int id;
	char name[NAME_LEN];
	char** courses;
};

struct StudentListNode{
	struct Student data;
	struct StudentListNode* next;
};

struct StudentListNode  *studFirstNode = NULL;

#endif
