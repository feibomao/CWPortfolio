#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

#include "course.h"
#include "student.h"

#define lineLen 50

void readInputFrom(char* fileName)
{

	FILE* studInfo = fopen(fileName, "r");
	
	char line[lineLen];
	//char line2[lineLen];

	char currStud[lineLen];
	//char currID[lineLen];
	int currID;
	char code[5];

	int iStud = -1;
	int iCourse;
	//fgets(line2, lineLen, studInfo);


	while(fscanf(studInfo, "%s", line) != EOF){
		printf("init: %s\n", line);
		if(strcmp(line, "Student") == 0){
			iStud ++;
			fscanf(studInfo, "%d", &currID);
			fscanf(studInfo, " %s", currStud);

			printf("|%d|\n", currID);
			printf("|%s|\n", currStud);

			studentNames[iStud] = currStud;
			studentIDs[iStud] = currID;
		}
		else{
			//code = (char*) malloc(5*sizeof(char));
			
			fscanf(studInfo, "%s", code);

			printf("%s\n",code);
			
			for(int i = 0; i < 20; i++){
				if(courseIDs[i] != NULL){
					printf("icourse %s\n", courseIDs[i]);
				}
			}
                               
			for(int i = 0; i < 20; i++){
				//printf("%s\n", code);
						
				if(courseIDs[i] == NULL){
					printf("new course\n");
					iCourse = i;
					courseIDs[i] = &code;
					printf("%s\n", courseIDs[i]);
					goto gottem;
				}
				else if(strcmp(code, courseIDs[i]) == 0){
					printf("%s\n", &code);
					printf("%s\n", courseIDs[i]);
					printf("existing course\n");
					iCourse = i;
					goto gottem;
				}
			}

gottem:

			printf("%d, free\n", iCourse);
			//free(code);
        		//for(int i = 0; i < 20; i++){
			//	if(courseIDs[i] != NULL){
              		//		printf("icourse %s\n", courseIDs[i]);
        		//	}
			//}


			//
			//courseIDs[find(code,courseIDs)] = code;
			//if(find(code, courseIDs) == -1){
				
			//}
		}
		printf("break\n");
		//printf("%s", line);
        //	fscanf(studInfo, "%s", line);
	}
	

	//printf("%s", line);

	//fscanf(studInfo, "%s", line);

	//for(int i = 0; i < 20; i++){
       // 	printf("%d\n", studentIDs[i]);
	//}
}

void writeOutputTo(char* fileName)
{
}
 
void cleanup()
{
}

int main(int argc, char** argv)
{
  char* inputFile = "studentInfo.txt";
  //char* outputFile = "courseInfo.txt";
  //if(argc == 3) {
  //  inputFile = argv[1];
  //  outputFile = argv[2];
  //}
  readInputFrom(inputFile);
  //writeOutputTo(outputFile);
  //cleanup();
  return 0;
}  

