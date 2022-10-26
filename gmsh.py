import gmsh
import sys
import os
import numpy as np
import time
import math
start_time = time.time()

wdir="/mnt/2/cases_for_paper/"

gmsh.initialize(sys.argv) # init gmsh
gmsh.model.add("boolean")
#
occ = gmsh.model.occ        # opencascade cad
option = gmsh.option        # gmsh options
mesh = gmsh.model.mesh  # mesh
field=gmsh.model.mesh.field
# msh2 options
option.setNumber("Mesh.PartitionOldStyleMsh2", 1)
option.setNumber("Mesh.CreateTopologyMsh2", 1)
option.setNumber("Mesh.PartitionConvertMsh2", 0)
option.setNumber("Mesh.PreserveNumberingMsh2", 1)
option.setNumber("Mesh.SaveTopology", 1)
# gui options
option.setNumber("General.ExpertMode", 0)  # show dialogs
option.setNumber("General.Antialiasing", 1)  # smooth
option.setNumber("General.DoubleBuffer", 1)  # visual
option.setNumber("Geometry.NumSubEdges", 1000) # nicer geo display

# occ geometry options
option.setNumber("Geometry.OCCBoundsUseStl", 1)  # more accurate boundaries
option.setNumber("Geometry.OCCUseGenericClosestPoint", 0)  # slower, more accurate
option.setNumber("Geometry.OCCImportLabels", 0)  # copy labels from import
option.setNumber("Geometry.OCCParallel", 1)  # use all procs
option.setNumber("Geometry.Tolerance", 1e-16)  # tolerance
option.setNumber("Mesh.StlLinearDeflection", 1e-7)
option.setNumber("Mesh.StlAngularDeflection", 1e-2)
delta = 0.003
flag1=10000000
flag2=20000000
flag3=30000000
flag4=40000000
############implementation of all variants D_in###############
variantsD=[] 
for i in np.arange(0.002, 0.005, 0.001):
	variantsD.append(round(i, 3))
##############################################################
########implementation of all variants H-blin hight###########
variantsH=[] 
for i in np.arange(0.002, 0.009, 0.001):
	variantsH.append(round(i, 3))
##############################################################
########implementation of all variants R-blin radius###########
variantsR=[] 
for i in np.arange(0.003, 0.0805, 0.0005):
	variantsR.append(round(i, 4))
##############################################################
counter=0
for NumR in range(2,len(variantsR)+1,2):#POMENAY NA 2!!!!!!
	for d in variantsD:
		print('d=',d)
		for H in variantsH:
			print('H=',H)
			for SizeShift in range(len(variantsR)):
				print('SizeShift=',SizeShift)
				counter=0
				break_out_flag = False
				XShift=0
				if ((len(variantsR[variantsR.index(variantsR[0]) + SizeShift:NumR]) < SizeShift) or (len(variantsR[variantsR.index(variantsR[0])+SizeShift:NumR]) == 1)):
					print('BREAK2SHIFT')
					break
				while XShift<variantsR[-1]:
					if (counter>0):
						print('COUNTER>0')
						break
					break_out_flag2 = False
					XShift2=0
					while XShift2<variantsR[-1]:
						if (counter>0):
							print('COUNTER>0')
							break
						break_out_flag3 = False
						gmsh.model.removePhysicalGroups()
						gmsh.model.removeEntities(occ.getEntities(3),True)
						occ.remove(occ.getEntities(3))
						gmsh.model.removeEntities(occ.getEntities(2),True)
						occ.remove(occ.getEntities(2))
						gmsh.model.removeEntities(occ.getEntities(1),True)
						occ.remove(occ.getEntities(1))
						gmsh.model.removeEntities(occ.getEntities(0),True)
						occ.remove(occ.getEntities(0))
						print('XShift=',XShift)
						print('XShift2=',XShift2)
						start_case_time = time.time()
						coordinataXup=0
						coordinataXdown=0
						Hhs=[]
						for r in variantsR[variantsR.index(variantsR[0])+SizeShift:NumR:2]:
							#
							print('r=',r,'indexR=',variantsR.index(r),'coordinataXup=',coordinataXup)
							#
							if (len(variantsR[variantsR.index(variantsR[0])+SizeShift:NumR])<3):
								print('BREAK LEN < 3')
								break
							if ((variantsR.index(r)-SizeShift)<1):
								Hh0=0
								Hh0=(variantsR[variantsR.index(r)+1]*2-d)/2
								Step1=0
								Step1=r*2-delta-Hh0
								coordinataXup=round(5*(H*4)+(r-Step1),4)
								print('Step1=',Step1,'5*(H*4)=',5*(H*4),'(r-Step1)=',(r-Step1))
								Hhs.append(round(((coordinataXup+r-XShift)-5*(H*4)-delta),4))
								if ((r*2-Step1)-delta-XShift)<Step1:
									break_out_flag = True
									print('BREAK1')
									break
							#
							if ((variantsR.index(r)-SizeShift)>1):
								Hhs.append(round((coordinataXdown-(coordinataXup-XShift)-d),4))
								coordinataXup=round(coordinataXup+d+r,4)
							#
							occ.addCylinder(x=coordinataXup-XShift,y=H/2,z=0,dx=0,dy=H,dz=0,r=r,tag=(variantsR.index(r)+1))
							coordinataXup=round(coordinataXup+r,4)
							if (len(Hhs)>1 and (Hhs[-1]< Hhs[-2])):
								break_out_flag3 = True
							if (NumR==variantsR.index(r)+1):
								print('BREAK2')
								break
							#
							if (((variantsR.index(r)+1)-SizeShift)<2):
								coordinataXdown=round(5*(H*4)+delta+variantsR[variantsR.index(r)+1],4)
							#
							if (((variantsR.index(r)+1)-SizeShift)>2):
								Hhs.append(round((coordinataXup-XShift-(coordinataXdown+d)),4))
								coordinataXdown=round(coordinataXdown+d+variantsR[variantsR.index(r)+1],4)
							#
							occ.addCylinder(x=coordinataXdown,y=0,z=0,dx=0,dy=H/2,dz=0,r=variantsR[variantsR.index(r)+1],tag=((variantsR.index(r)+1)+2+len(variantsR)))
							coordinataXdown=round(coordinataXdown+variantsR[variantsR.index(r)+1],4)
							if ((coordinataXup+d)>coordinataXdown):
								break_out_flag2 = True
						if break_out_flag2:
							print('BREAK3!')
							break
						if break_out_flag3:
							print('holes get smaller')
							XShift2=XShift2+0.0005
							continue
						if break_out_flag:
							print('BREAK3')
							break
						if ((len(variantsR[variantsR.index(variantsR[0])+SizeShift:NumR])% 2) != 0):
							coordinataXout=coordinataXdown+delta+XShift2
							print('UNeven','coordinataXout=',coordinataXout)
							if (coordinataXout>(coordinataXup-XShift-Step1)):
								print('BREAK4up')
								break
						else:
							coordinataXout=coordinataXup+delta+XShift2
							print('even','coordinataXout=',coordinataXout)
							if (coordinataXout>coordinataXdown):
								print('BREAK4down')
								break
						if ((1.5*r)/(4*H))>= 1:
							coefficientR=1.5*r
						if ((1.5*r)/(4*H))< 1:
							coefficientR=4*H
						occ.addCylinder(x=0,y=0,z=0,dx=	5*(H*4),dy=0,dz=0,r=coefficientR,tag=(1000000))
						occ.addCylinder(x=coordinataXout,y=0,z=0,dx=15*(H*4),dy=0,dz=0,r=coefficientR,tag=(2000000))
						occ.synchronize()
						print("Build all cylinders Case")
						listOfVoluems=occ.getEntities(3)
						occ.synchronize()
						occ.fuse([(3,(1000000))],listOfVoluems,(3000000))
						print("All cylinders are united Case")
						occ.synchronize()
						checklistOfVoluems=occ.getEntities(3)
						occ.addBox(x=0,y=-coefficientR,z=0,dx=(coordinataXout+15*(H*4)),dy=coefficientR*2,dz=coefficientR,tag=4000000)
						occ.synchronize()
						occ.cut([(3,(3000000))],[(3,(4000000))],(5000000))
						occ.addBox(x=0,y=-coefficientR,z=-coefficientR,dx=(coordinataXout+15*(H*4)),dy=coefficientR,dz=coefficientR,tag=(6000000))
						occ.cut([(3,(5000000))],[(3,(6000000))],(7000000))
						print("All cylinders are cut Case")
						occ.synchronize()
						#gmsh.fltk.run()
						eps = 1e-4
						eps2 = 1e-5
						xmin=0.0#coordinates[0]
						xmax=coordinataXout+15*(H*4)#coordinates[3]
						ymin=0.0#coordinates[1]
						ymax=coefficientR#coordinates[4]
						zmin=-coefficientR#coordinates[2]
						zmax=0#coordinates[5]
						flag1=flag1+1
						flag2=flag2+1
						flag3=flag3+1
						flag4=flag4+1
						listxy=occ.getEntitiesInBoundingBox(xmin-eps, ymin-eps, zmax-eps, xmax+eps, ymax+eps, zmax+eps, 2)
						xy=[listxy[i][1] for i in range(0,len(listxy))]
						listxz=occ.getEntitiesInBoundingBox(xmin-eps, ymin-eps, zmin-eps, xmax+eps, ymin+eps, zmax+eps, 2)
						xz=[listxz[i][1] for i in range(0,len(listxz))]
						listinflow=occ.getEntitiesInBoundingBox(xmin-eps, ymin-eps, zmin-eps, xmin+eps, ymax+eps, zmax+eps, 2)
						inflow=[listinflow[i][1] for i in range(0,len(listinflow))]
						listoutflow=occ.getEntitiesInBoundingBox(xmax-eps, ymin-eps, zmin-eps, xmax+eps, ymax+eps, zmax+eps, 2)
						outflow=[listoutflow[i][1] for i in range(0,len(listoutflow))]
						listinterior = occ.getEntitiesInBoundingBox(xmin-eps, ymin-eps, zmin-eps, xmax+eps, ymax+eps, zmax+eps, 3)
						interior=[listinterior[i][1] for i in range(0,len(listinterior))]
						listss2=occ.getEntities(2)
						ss=[listss2[i][1] for i in range(0,len(listss2))]
						wall=list(set(ss)-set(xy)-set(xz)-set(inflow)-set(outflow))
						option.setNumber("Mesh.Algorithm", 6)
						option.setNumber("Mesh.MeshSizeMin", 0.00009)
						option.setNumber("Mesh.MeshSizeMax", 0.0005)
						option.setNumber("Mesh.MeshSizeFromCurvature", 20) # calculate mesh size based on curvature
						option.setNumber("Mesh.SmoothRatio", 3)
						option.setNumber("Mesh.AnisoMax", 1000)
						option.setNumber("Mesh.StlLinearDeflection", 1e-7)
						option.setNumber("Mesh.StlAngularDeflection", 1e-2)
						occ.synchronize()
						#
						print(flag1)
						field.add("Box", flag1)
						field.setNumber(flag1, "VIn", 0.00025)
						field.setNumber(flag1, "XMin", 5*(H*4)-H*3)
						field.setNumber(flag1, "XMax", 5*(H*4))
						field.setNumber(flag1, "YMin", 0.0)
						field.setNumber(flag1, "YMax", coefficientR)
						field.setNumber(flag1, "ZMin", -coefficientR)
						field.setNumber(flag1, "ZMax", 0.0)
						field.setNumber(flag1, "Thickness", 0.000004)
						occ.synchronize()
						print('Done')
						#
						#
						print(flag2)
						field.add("Box", flag2)
						field.setNumber(flag2, "VIn", 0.00009)
						field.setNumber(flag2, "XMin", 5*(H*4))
						field.setNumber(flag2, "XMax", coordinataXout)
						field.setNumber(flag2, "YMin", 0.0)
						field.setNumber(flag2, "YMax", coefficientR)
						field.setNumber(flag2, "ZMin", -coefficientR)
						field.setNumber(flag2, "ZMax", 0.0)
						field.setNumber(flag2, "Thickness", 0.00004)
						occ.synchronize()
						print('Done')
						#
						print(flag3)
						field.add("Box", flag3)
						field.setNumber(flag3, "VIn", 0.00025)
						field.setNumber(flag3, "XMin", coordinataXout)
						field.setNumber(flag3, "XMax", (coordinataXout+15*(H*3)/10))
						field.setNumber(flag3, "YMin", 0.0)
						field.setNumber(flag3, "YMax", coefficientR)
						field.setNumber(flag3, "ZMin", -coefficientR)
						field.setNumber(flag3, "ZMax", 0.0)
						field.setNumber(flag3, "Thickness", 0.000004)
						print('Done')
						occ.synchronize()
						gmsh.model.mesh.field.add("Min", flag4)#MinAniso
						gmsh.model.mesh.field.setNumbers(flag4, "FieldsList", [(flag1),(flag2),(flag3)])#17, 16, 15, 14, 13, 12, 11, 10,9,
						field.setAsBackgroundMesh(flag4)
						occ.synchronize()
						gmsh.model.addPhysicalGroup(2, inflow, 1)
						gmsh.model.addPhysicalGroup(2, outflow, 2)
						gmsh.model.addPhysicalGroup(2, wall, 3)
						gmsh.model.addPhysicalGroup(2, xy, 4)
						gmsh.model.addPhysicalGroup(2, xz, 5)
						gmsh.model.addPhysicalGroup(3, interior, 1)
						occ.synchronize()
						#gmsh.fltk.run()
						# addPhysicalGroup(dim, phys_group_tag, name):
						gmsh.model.setPhysicalName(2, 1, "inlet")
						gmsh.model.setPhysicalName(2, 2, "outlet")
						gmsh.model.setPhysicalName(2, 3, "wall")
						gmsh.model.setPhysicalName(2, 4, "sym_1")
						gmsh.model.setPhysicalName(2, 5, "sym_2")
						gmsh.model.setPhysicalName(3, 1, "interior")
						occ.synchronize()
						mesh.generate(3)
						occ.synchronize()
						#gmsh.fltk.run()
						P1=str(H)
						P2=str(SizeShift)
						P3=str(XShift)
						P4=str(XShift2)
						P5=str(NumR)
						print(P5)
						P6=str(d)
						gmsh.write("geom.H="+P1+"_SizeShift="+P2+"_XShift="+P3+"_XShift2="+P4+"_Num_r="+P5+"_d="+P6+".msh2")  # OpenCascade geom
						print("-------------------------------------- %s seconds for case --------------------------------------" % (time.time() - start_case_time))
						counter=counter+1
						XShift2=XShift2+0.0005
					XShift=XShift+0.0005
gmsh.finalize()
print("----------------------------------- %s seconds for executing -----------------------------------" % (time.time() - start_time))
