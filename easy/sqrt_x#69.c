int mySqrt(int x)
{
	for(long i=1;i<=(int)(x/2)+1;i++)
	{
	    if(i*i>x)
	        return i-1;
	    if(i*i==x)
	        return i;
	}
	return 0;
}
