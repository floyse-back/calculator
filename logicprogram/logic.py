import math



class VectorProps():
    def __init__(self):
        pass


    def sum_vectors(self,vector1,vector2):
        return [vector1[i]+vector2[i] for i in range(0,len(vector1))]

    def subtraction_vector(self,vector1,vector2):
        return [vector1[i]-vector2[i] for i in range(0,len(vector1))]

    def scalar_vector(self,vector1,vector2):
        return sum([vector1[i]*vector2[i] for i in range(len(vector1))])

    def add_const_vector(self,vector,k):
        return [k*i for i in vector]

    def multiplication_vector(self,vector1,vector2):
        if len(vector1)==3:
            ax,ay,az=vector1
            bx,by,bz=vector2
            c=[ay*bz-az*by,az*bx-ax*bz,ax*by-ay*bx]
            return c
        elif len(vector1)==2:
            pass

    def module_vector(self,vector1,vector2=None):
        if vector2:
            return math.sqrt(sum([(vector1[i]-vector2[i])**2 for i in range(len(vector1))]))
        else:
            return math.sqrt(sum([vector1[i]**2 for i in range(len(vector1))]))


    def unitate_vector(self,vector1):
        return [vector1[i]/self.module_vector(vector1) for i in range(len(vector1))]

    def angle_vector(self,vector1,vector2):
        cosa=(self.scalar_vector(vector1, vector2))/(self.module_vector(vector1)*self.module_vector(vector2))
        return "%.1f" % math.degrees(cosa)

    def collinear_vector(self,vector1,vector2):
        n=[]
        """
        return 1 - колінеарні
        return 2 - не колінеарні
        """
        for i in range(0,len(vector1)):
            if vector1[i]==0 and vector2[i] ==0:
                n.append(0)
            elif vector2[i]==0 or vector1[i]==0:
                return 2
            else:
                n.append(vector1[i]/vector2[i])
        for i in range(len(n)-1):
            if n[i]!=0 and n[i]!=n[i+1]:
                return 2
        return 1







Vec=VectorProps()
print(Vec.sum_vectors(vector1=[10,5,2],vector2=[15,24,3]))
print(Vec.subtraction_vector(vector1=[10,5,2],vector2=[15,24,3]))
print(Vec.add_const_vector(vector=[10,5,2],k=6))
print(Vec.scalar_vector(vector1=[10,5,2],vector2=[15,24,3]))
print(Vec.multiplication_vector(vector1=[-1,2,-2],vector2=[2,1,-1]))
print(Vec.module_vector(vector1=[2,-1],vector2=[5,3]))
print(Vec.unitate_vector(vector1=[3,4]))
print(Vec.angle_vector(vector1=[3,4],vector2=[5,12]))
print(Vec.collinear_vector([3,4],[6,8]))