#include <stdio.h>

main(){
	float height, weight, bmi;
	printf("身高(cm)：");
	scanf("%f", &height);
	printf("體重(kg)：");
	scanf("%f", &weight);
	bmi=weight/((height/100)*(height/100));
	printf("\n您的BMI：%.1f\n",bmi);
	if(bmi<18.5){
		printf("您的體重過輕！\n");
	}else if(bmi<24){
		printf("您的體重正常！\n");
	}else{
		printf("您的體重過重！\n");
	}
	system("PAUSE");
}
