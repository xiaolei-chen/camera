% ʹ��matlab��֤modelview����

posX = 3;    % ����λ��
posY = -2;
posZ = 4;

rotX = 15;   % ������ת�Ƕ�
rotY = 14;
rotZ = 14;

camX = 3;   % �����λ��
camY = -2;
camZ = 10;
pitch = 14;  % ��X��
heading = 10; % ��Y��
roll = 14;   % ��Z��

% ת�ɻ���
rotX = deg2rad(rotX);
rotY = deg2rad(rotY);
rotZ = deg2rad(rotZ);

% ģ��ƽ�ƾ���
tran_matrix = [
   1 0 0 posX
   0 1 0 posY
   0 0 1 posZ
   0 0 0 1];

% ģ����Z��ת����
rotZ_matrix = [ 
   cos(rotZ) -sin(rotZ) 0 0
   sin(rotZ)  cos(rotZ) 0 0
   0          0         1 0
   0          0         0 1];
% ģ����Y��ת����
rotY_matrix = [
   cos(rotY)  0 sin(rotY) 0
   0          1 0         0
   -sin(rotY) 0 cos(rotY) 0
   0          0 0         1];
% ģ����X��ת����
rotX_matrix = [
   1 0         0          0
   0 cos(rotX) -sin(rotX) 0
   0 sin(rotX) cos(rotX)  0
   0 0         0          1];
   
   %ģ�;���
model =  tran_matrix * rotX_matrix * rotY_matrix * rotZ_matrix * eye(4);
model

% ת�ɻ���
pitch = deg2rad(pitch);
heading = deg2rad(heading);
roll = deg2rad(roll);

% ��ͼƽ�ƾ���
tran_matrix = [
   1 0 0 -camX
   0 1 0 -camY
   0 0 1 -camZ
   0 0 0 1];
% ģ����Z��ת����
rotZ_matrix = [ 
   cos(-roll) -sin(-roll) 0 0
   sin(-roll)  cos(-roll) 0 0
   0          0         1 0
   0          0         0 1];
% ģ����Y��ת����
rotY_matrix = [
   cos(-heading)  0 sin(-heading) 0
   0              1 0         0
   -sin(-heading) 0 cos(-heading) 0
   0              0 0         1];
% ģ����X��ת����
rotX_matrix = [
   1 0           0          0
   0 cos(-pitch) -sin(-pitch) 0
   0 sin(-pitch) cos(-pitch)  0
   0 0           0          1];
   
view = rotZ_matrix * rotY_matrix  * rotX_matrix * tran_matrix * eye(4);
view
modelview = view * model