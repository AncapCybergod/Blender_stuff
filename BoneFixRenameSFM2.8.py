import bpy, mathutils, fnmatch

class ExitOK(Exception):
    pass
	
bpy.ops.object.mode_set(mode='EDIT')
edit_bones = bpy.context.object.data.edit_bones


Allbones = (
("Pelvis", "ValveBiped.Bip01_pelvis", "bip_pelvis", "ValveBiped.Bip01_Spine", "pelvis"),
("Spine0", "ValveBiped.Bip01_Spine1", "bip_spine_0", "ValveBiped.Bip01_Spine1", "abdomenLower"),
("Spine1", "ValveBiped.Bip01_Spine2", "bip_spine_1", "ValveBiped.Bip01_Spine2", "abdomenUpper"),
("Spine2", "ValveBiped.Bip01_Spine3", "bip_spine_2", "ValveBiped.Bip01_Spine3", "chestLower"),
("Spine3", "ValveBiped.Bip01_Spine4", "bip_spine_3", "ValveBiped.Bip01_Spine4", "chestUpper"),
("Neck0", "ValveBiped.Bip01_Neck1", "bip_neck", "neckLower"),
("Neck1", "neckUpper"),
("Head", "ValveBiped.Bip01_Head1", "bip_head", "head"),

("Collar_L", "ValveBiped.Bip01_L_Clavicle", "bip_collar_L", "lCollar"),
("UpperArm_L", "ValveBiped.Bip01_L_UpperArm", "bip_upperArm_L", "lShldrBend"),
("UpperArmTwist_L", "lShldrTwist"),
("LowerArm_L", "ValveBiped.Bip01_L_Forearm", "bip_lowerArm_L", "lForearmBend"),
("LowerArmTwist_L", "lForearmTwist"),
("Hand_L", "ValveBiped.Bip01_L_Hand", "bip_hand_L", "lHand"),

("Collar_R", "ValveBiped.Bip01_R_Clavicle", "bip_collar_R", "rCollar"),
("UpperArm_R", "ValveBiped.Bip01_R_UpperArm", "bip_upperArm_R", "rShldrBend"),
("UpperArmTwist_R", "rShldrTwist"),
("LowerArm_R", "ValveBiped.Bip01_R_Forearm", "bip_lowerArm_R", "rForearmBend"),
("LowerArmTwist_R", "rForearmTwist"),
("Hand_R", "ValveBiped.Bip01_R_Hand", "bip_hand_R", "rHand"),



("FingerThumb0_L", "ValveBiped.Bip01_L_Finger0", "bip_thumb_0_L", "lThumb1"),
("FingerThumb1_L", "ValveBiped.Bip01_L_Finger01", "bip_thumb_1_L", "lThumb2"),
("FingerThumb2_L", "ValveBiped.Bip01_L_Finger02", "bip_thumb_2_L", "lThumb3"),
("FingerIndex0_L", "ValveBiped.Bip01_L_Finger1", "bip_index_0_L", "lIndex1"),
("FingerIndex1_L", "ValveBiped.Bip01_L_Finger11", "bip_index_1_L", "lIndex2"),
("FingerIndex2_L", "ValveBiped.Bip01_L_Finger12", "bip_index_2_L", "lIndex3"),
("FingerMiddle0_L", "ValveBiped.Bip01_L_Finger2", "bip_middle_0_L", "lMid1"),
("FingerMiddle1_L", "ValveBiped.Bip01_L_Finger21", "bip_middle_1_L", "lMid2"),
("FingerMiddle2_L", "ValveBiped.Bip01_L_Finger22", "bip_middle_2_L", "lMid3"),
("FingerRing0_L", "ValveBiped.Bip01_L_Finger3", "bip_ring_0_L", "lRing1"),
("FingerRing1_L", "ValveBiped.Bip01_L_Finger31", "bip_ring_1_L", "lRing2"),
("FingerRing2_L", "ValveBiped.Bip01_L_Finger32", "bip_ring_2_L", "lRing3"),
("FingerPinky0_L", "ValveBiped.Bip01_L_Finger4", "bip_pinky_0_L", "lPinky1"),
("FingerPinky1_L", "ValveBiped.Bip01_L_Finger41", "bip_pinky_1_L", "lPinky2"),
("FingerPinky2_L", "ValveBiped.Bip01_L_Finger42", "bip_pinky_2_L", "lPinky3"),

("FingerThumb0_R", "ValveBiped.Bip01_R_Finger0", "bip_thumb_0_R", "rThumb1"),
("FingerThumb1_R", "ValveBiped.Bip01_R_Finger01", "bip_thumb_1_R", "rThumb2"),
("FingerThumb2_R", "ValveBiped.Bip01_R_Finger02", "bip_thumb_2_R", "rThumb3"),
("FingerIndex0_R", "ValveBiped.Bip01_R_Finger1", "bip_index_0_R", "rIndex1"),
("FingerIndex1_R", "ValveBiped.Bip01_R_Finger11", "bip_index_1_R", "rIndex2"),
("FingerIndex2_R", "ValveBiped.Bip01_R_Finger12", "bip_index_2_R", "rIndex3"),
("FingerMiddle0_R", "ValveBiped.Bip01_R_Finger2", "bip_middle_0_R", "rMid1"),
("FingerMiddle1_R", "ValveBiped.Bip01_R_Finger21", "bip_middle_1_R", "rMid2"),
("FingerMiddle2_R", "ValveBiped.Bip01_R_Finger22", "bip_middle_2_R", "rMid3"),
("FingerRing0_R", "ValveBiped.Bip01_R_Finger3", "bip_ring_0_R", "rRing1"),
("FingerRing1_R", "ValveBiped.Bip01_R_Finger31", "bip_ring_1_R", "rRing2"),
("FingerRing2_R", "ValveBiped.Bip01_R_Finger32", "bip_ring_2_R", "rRing3"),
("FingerPinky0_R", "ValveBiped.Bip01_R_Finger4", "bip_pinky_0_R", "rPinky1"),
("FingerPinky1_R", "ValveBiped.Bip01_R_Finger41", "bip_pinky_1_R", "rPinky2"),
("FingerPinky2_R", "ValveBiped.Bip01_R_Finger42", "bip_pinky_2_R", "rPinky3"),

("Thigh_L", "ValveBiped.Bip01_L_Thigh", "bip_hip_L", "lThighBend"),
("ThighTwist_L", "lThighTwist"),
("Shin_L", "ValveBiped.Bip01_L_Calf", "bip_knee_L", "lShin"),
("Foot_L", "ValveBiped.Bip01_L_Foot", "bip_foot_L", "lFoot"),

("Thigh_R", "ValveBiped.Bip01_R_Thigh", "bip_hip_R", "rThighBend"),
("ThighTwist_R", "rThighTwist"),
("Shin_R", "ValveBiped.Bip01_R_Calf", "bip_knee_R", "rShin"),
("Foot_R", "ValveBiped.Bip01_R_Foot", "bip_foot_R", "rFoot"),

)

ConnectBones = (
"Spine0", "Spine1", "Spine2", "Spine3", "Neck0", "Neck1", "Head",

"LowerArm_L", "Hand_L", "Shin_L", "Foot_L",
"LowerArm_R", "Hand_R", "Shin_R", "Foot_R",

"FingerThumb1_L", "FingerThumb2_L", "FingerIndex1_L", "FingerIndex2_L", "FingerMiddle1_L", "FingerMiddle2_L", "FingerRing1_L", "FingerRing2_L", "FingerPinky1_L", "FingerPinky2_L", 
"FingerThumb1_R", "FingerThumb2_R", "FingerIndex1_R", "FingerIndex2_R", "FingerMiddle1_R", "FingerMiddle2_R", "FingerRing1_R", "FingerRing2_R", "FingerPinky1_R", "FingerPinky2_R", 

)

for bone in edit_bones:
	bpy.context.object.pose.bones[bone.name].custom_shape = None
	for subset,name in enumerate(Allbones):
		if bone.name in name:
			edit_bones[bone.name].name = Allbones[subset][0]
			
edit_bones["Hand_L"].parent = edit_bones["UpperArm_L"]
edit_bones["Hand_L"].tail = (edit_bones["Hand_L"].tail + edit_bones["FingerIndex0_L"].head + edit_bones["FingerMiddle0_L"].head + edit_bones["FingerRing0_L"].head + edit_bones["FingerPinky0_L"].head)/5
			
edit_bones["Hand_R"].parent = edit_bones["UpperArm_R"]
edit_bones["Hand_R"].tail = (edit_bones["Hand_R"].tail + edit_bones["FingerIndex0_R"].head + edit_bones["FingerMiddle0_R"].head + edit_bones["FingerRing0_R"].head + edit_bones["FingerPinky0_R"].head)/5

if bpy.context.object.data.edit_bones.get("ThighTwist_L") is not None:
	edit_bones["Shin_L"].parent = edit_bones["Thigh_L"]
	edit_bones["ThighTwist_L"].tail = edit_bones["Shin_L"].head				
	edit_bones["Shin_R"].parent = edit_bones["Thigh_R"]
	edit_bones["ThighTwist_R"].tail = edit_bones["Shin_R"].head
	
if bpy.context.object.data.edit_bones.get("UpperArmTwist_L") is not None:
	edit_bones["LowerArm_L"].parent = edit_bones["UpperArm_L"]
	edit_bones["UpperArmTwist_L"].tail = edit_bones["LowerArm_L"].head				
	edit_bones["LowerArm_R"].parent = edit_bones["UpperArm_R"]
	edit_bones["UpperArmTwist_R"].tail = edit_bones["LowerArm_R"].head	
	
if bpy.context.object.data.edit_bones.get("LowerArmTwist_L") is not None:
	edit_bones["Hand_L"].parent = edit_bones["LowerArm_L"]
	edit_bones["LowerArmTwist_L"].tail = edit_bones["Hand_L"].head				
	edit_bones["Hand_R"].parent = edit_bones["LowerArm_R"]
	edit_bones["LowerArmTwist_R"].tail = edit_bones["Hand_R"].head	

for bone in ConnectBones:
	#print (bone)
	if bpy.context.object.data.edit_bones.get(bone) is not None: 
		ParentBone = edit_bones[bone].parent				
		ParentBone.tail = edit_bones[bone].head
		edit_bones[bone].use_connect = True		



