#ifndef COURSE_H
#define COURSE_H

#define MAX_COURSE_NUM 20

struct Course{
	char id[5];
	char name[100];
	int enrollmentNum;
	int* students;
};

struct CourseListNode{
	struct Course data;
	struct CourseListNode* next;
};

struct CourseListNode  *courseFirstNode = NULL;

#endif
