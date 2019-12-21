import math
class eign():
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

    #####################################################

    def eigenvalues(self,equls,xval):
        ls =[]
        ls.append(xval)
        for eq in equls:
            xval = eq-xval
            # print("...",xval)
            ls.append(xval)
        print("ls",ls)
        return ls        
    ################################################################
    # #######################eign vaectors################################
    def matrixmins(self,matrix,eignval): 
        matminz = [[0,1,2],[0,1,2],[0,1,2]]
        for cnt1 in range(len(mat)):
            for cnt2 in range(len(mat)):
                if cnt1 == cnt2:
                    matminz[cnt1][cnt2] = mat[cnt1][cnt2]-eignval
                else:
                    matminz[cnt1][cnt2] = mat[cnt1][cnt2]

        x1 = (matminz[0][0]*matminz[1][1])-(matminz[1][0]*matminz[0][1])
        x2 = (matminz[0][1]*matminz[1][2])-(matminz[1][1]*matminz[0][2])
        x3 = (matminz[0][2]*matminz[1][0])-(matminz[1][2]*matminz[0][0])
        x = [x1,x2,x3]
        return x

    #############################matrix print########################
    def matrixprint(self,mat):
        for cnt1 in range(len(mat)):
            print(mat[cnt1])

    def factorize(self,a,b,c):
        sqvalue = (math.sqrt((b*b)-(4*a*c)))
        rot1 =((b*1)-sqvalue)/(2*a)
        rot2 =((b*1)+sqvalue)/(2*a)
        factorizls = [int(rot1),int(rot2)]
        return factorizls

        

    ########################MainController###################################
    def mainController(self,mat):
        ind1 =[1,0,0]
        ind2 =[0,1,0]
        ind3 =[0,0,1]

        indmat = [ind1,ind2,ind3]    
        ####################################################matrix printing
        print("matrinx\n")
        for matx in mat:
            print(matx)
        #####################################eign values finding
        s1 = self.s1fun(mat)
        s2 = self.s2fun(mat)
        s3 = self.s3fun(mat)
        equls=[s1,s2,s3]
        print("\ncharastric equations",equls)

        ################################################################
        divdls = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9,10,-10]
        for ls in divdls:
            rels = self.eigenvalues(equls,ls)
            if rels[-1]==0:
                print("\neign values....\n\n",rels)
                break
            else:
                print("try again")
        print(rels)
        factor = self.factorize(rels[0],rels[1],rels[2])
        print("eign vetors are \n")
        rels1 = [rels[0],factor[0],factor[1]]
        cnt = 0
        for eignval in rels1:
            cnt +=1
            print("eign vector values X",cnt)
            print(self.matrixmins(mat,eignval))

        



###############################################################
obj = eign()
# m1 = [1,2,0]
# m2 = [2,-1,0]
# m3 = [0,0,1]
# mat = [m1,m2,m3]
# m1 = [7,2,-2]
# m2 = [-6,-1,2]
# m3 = [6,2,-1]
# mat = [m1,m2,m3]
m1 = [8,-8,-2]
m2 = [4,-3,-2]
m3 = [3,-4,1]
mat = [m1,m2,m3]
obj.mainController(mat)




    