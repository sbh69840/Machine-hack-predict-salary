#include<stdio.h>
int main(){
	float h,u,d,f;
	int day = 1,suc=1;
	float total = 0,u_main=0;

	while(1){
		u_main = 0;
		total = 0;
		day = 1;
		suc = 1;
		
	scanf("%f %f %f %f\n",&h,&u,&d,&f);
	if(h!=0 || u!=0 || d!=0 || f!=0){
		while(total<=h){
			if((u-u_main)>=0){
				total+=(float)u;
			}
			if(total>h){
				break;
			}
			total-=(float)d;
			
			if(total<0){
				suc = 0;
				printf("failure on day %d\n",day);
				break;
			}
			if(day==1){
				u_main = (float)((f/100)*u);
			}
			if((u-u_main)>=0){
				u = u-u_main;
			}
			day+=1;
		}
		if(suc!=0){
			printf("success on day %d\n",day);

		}
	}else{
		break;
	}
}
return 0;
}
