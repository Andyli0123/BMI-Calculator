#include <stdio.h>

main(){
	float height, weight, bmi;
	printf("����(cm)�G");
	scanf("%f", &height);
	printf("�魫(kg)�G");
	scanf("%f", &weight);
	bmi=weight/((height/100)*(height/100));
	printf("\n�z��BMI�G%.1f\n",bmi);
	if(bmi<18.5){
		printf("�z���魫�L���I\n");
	}else if(bmi<24){
		printf("�z���魫���`�I\n");
	}else{
		printf("�z���魫�L���I\n");
	}
	system("PAUSE");
}
