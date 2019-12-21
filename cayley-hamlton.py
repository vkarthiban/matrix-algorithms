class caly():
    #################################################
    #finding charastric eqation 1
    def s1fun(self,mat):
        s1 = mat[0][0]+mat[1][1]+mat[2][2]
        return s1
    ######################################finding s2##################################
    #finding charastric eqation 2
    def s2fun(self,mat):
        x1 = [mat[1][1]*mat[2][2]][0]-[mat[2][1]*mat[1][2]][0]
        x2 = [mat[0][0]*mat[2][2]][0]-[mat[2][0]*mat[0][2]][0]
        x3 = [mat[0][0]*mat[1][1]][0]-[mat[1][0]*mat[0][1]][0]
        s2 = x1+x2+x3
        return s2

    ############################finding s3#############################
    #finding charastric eqation 3
    def s3fun(self,mat):
        z1 = [mat[1][1]*mat[2][2]][0]-[mat[2][1]*mat[1][2]][0]
        z2 = [mat[1][0]*mat[2][2]][0]-[mat[2][0]*mat[1][2]][0]
        z3 = [mat[1][0]*mat[2][1]][0]-[mat[2][0]*mat[1][1]][0]
        s3 = (mat[0][0]*z1)-(mat[0][1]*z2)+(mat[0][2]*z3)
        return s3

    #########################################matrixmultiply###################################
    ###matrix multiplicaation##############
    def matrixMul(self,mat1,mat2):
        mainls = [0,1,2]
        for cnt1 in range(len(mat1)):
            lst1 = [0,1,2]
            for cnt2 in range(len(mat1[cnt1])):
                lst1[cnt2] = self.matmul2(cnt1,cnt2,mat1,mat2)
            mainls[cnt1] = self.matAdd(lst1)
        return mainls

    def matmul2(self,cnt1,cnt2,mat1,mat2):
        lst=[0,1,2]
        for cnt3 in range(len(mat1)):
            lst[cnt3] = mat1[cnt1][cnt2]*mat2[cnt2][cnt3]
        return lst  

    def matAdd(self,mat1):
        varls=[]
        for cnt1 in range(len(mat1)):
            print(" ")
            vars = 0
            for cnt2 in range(len(mat1)):
                var = mat1[cnt2][cnt1]
                vars += var
            varls.append(vars)
        return varls

    #################################valmat##############################
    #matrix with single value multiplication
    def valMatMul(self,val,matx):
        matc = [[0,1,2],[0,1,2],[0,1,2]]
        for cnt1 in range(len(matx)):
            for cnt2 in range(len(matx)):
                matc[cnt1][cnt2]=val*matx[cnt1][cnt2]
        return matc

    ####################################veryfy calyhamlton###############################
    #verify calyhamlton final value is all position is zero
    def veryfyCaly(self,matx,Ax,A3,indmat,eignls):
        AX2mat = self.valMatMul(eignls[0],Ax)  
        Amat = self.valMatMul(eignls[1],matx)
        verifycaly = [[0,1,2],[0,1,2],[0,1,2]]
        indmats = self.valMatMul(eignls[2],indmat)
        for cnt1 in range(len(matx)):
            for cnt2 in range(len(matx)):
                verifycaly[cnt1][cnt2] = A3[cnt1][cnt2]+AX2mat[cnt1][cnt2]+Amat[cnt1][cnt2]+indmats[cnt1][cnt2]          
        return verifycaly


    #############################matrix print########################
    def matrixprint(self,mat):
        for cnt1 in range(len(mat)):
            print(mat[cnt1])

    ########################MainController###################################
    def mainController(self,mat):
        #####################identy matrix##############################
        ind1 =[1,0,0]
        ind2 =[0,1,0]
        ind3 =[0,0,1]

        indmat = [ind1,ind2,ind3]    
        ####################################################matrix printing
        print("matrinx")
        for matx in mat:
            print(matx)
        #####################################eign values finding
        s1 = self.s1fun(mat)
        s2 = self.s2fun(mat)
        s3 = self.s3fun(mat)
        equls=[s1,s2,s3]
        print("eign values are",equls)
        ###################################finding Asquare and aQube########################
        A2 = self.matrixMul(mat,mat)
        print("ASquare matrix")
        self.matrixprint(A2)

        ################A3finding
        A3 = self.matrixMul(A2,mat)
        print("Aqube matrix")
        self.matrixprint(A3)
        eignls1 = [(s1*-1),s2,(s3*-1)]
        #############################################verify clayhamlton###################################
        calyreturn = self.veryfyCaly(mat,A2,A3,indmat,eignls1)
        print("calyreturn")
        self.matrixprint(calyreturn)





###############################################################
obj = caly()
m1 = [1,2,0]
m2 = [2,-1,0]
m3 = [0,0,1]
mat = [m1,m2,m3]
obj.mainController(mat)



##############################################################    

#Amartix algorithm
####A4=S1*(S1*A2)+S1*(s2*A)+S1*(s3*I)+s2*A2+S3*A

##A3=S1*A2+s2*A+s3*I
##A4=s1*A3+s2*A2+S3*A
##A4=S1*(A3)+s2*A2+S3*A


###########example matrix##############
    # m1 = [4,3,1]
    # m2 = [2,1,-2]
    # m3 = [1,2,1]
    # mat = [m1,m2,m3]


        # m1 = [7,2,-2]
    # m2 = [-6,-1,2]
    # m3 = [6,2,-1]
    # mat = [m1,m2,m3]