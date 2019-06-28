% 使用matlab验证modelview矩阵

posX = 3;    % 物体位置
posY = -2;
posZ = 4;

rotX = 15;   % 物体旋转角度
rotY = 14;
rotZ = 14;

camX = 3;   % 摄像机位置
camY = -2;
camZ = 10;
pitch = 14;  % 绕X轴
heading = 10; % 绕Y轴
roll = 14;   % 绕Z轴

% 转成弧度
rotX = deg2rad(rotX);
rotY = deg2rad(rotY);
rotZ = deg2rad(rotZ);

% 模型平移矩阵
tran_matrix = [
   1 0 0 posX
   0 1 0 posY
   0 0 1 posZ
   0 0 0 1];

% 模型绕Z旋转矩阵
rotZ_matrix = [ 
   cos(rotZ) -sin(rotZ) 0 0
   sin(rotZ)  cos(rotZ) 0 0
   0          0         1 0
   0          0         0 1];
% 模型绕Y旋转矩阵
rotY_matrix = [
   cos(rotY)  0 sin(rotY) 0
   0          1 0         0
   -sin(rotY) 0 cos(rotY) 0
   0          0 0         1];
% 模型绕X旋转矩阵
rotX_matrix = [
   1 0         0          0
   0 cos(rotX) -sin(rotX) 0
   0 sin(rotX) cos(rotX)  0
   0 0         0          1];
   
   %模型矩阵
model =  tran_matrix * rotX_matrix * rotY_matrix * rotZ_matrix * eye(4);
model

% 转成弧度
pitch = deg2rad(pitch);
heading = deg2rad(heading);
roll = deg2rad(roll);

% 视图平移矩阵
tran_matrix = [
   1 0 0 -camX
   0 1 0 -camY
   0 0 1 -camZ
   0 0 0 1];
% 模型绕Z旋转矩阵
rotZ_matrix = [ 
   cos(-roll) -sin(-roll) 0 0
   sin(-roll)  cos(-roll) 0 0
   0          0         1 0
   0          0         0 1];
% 模型绕Y旋转矩阵
rotY_matrix = [
   cos(-heading)  0 sin(-heading) 0
   0              1 0         0
   -sin(-heading) 0 cos(-heading) 0
   0              0 0         1];
% 模型绕X旋转矩阵
rotX_matrix = [
   1 0           0          0
   0 cos(-pitch) -sin(-pitch) 0
   0 sin(-pitch) cos(-pitch)  0
   0 0           0          1];
   
view = rotZ_matrix * rotY_matrix  * rotX_matrix * tran_matrix * eye(4);
view
modelview = view * model