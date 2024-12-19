function [mapping,eigvalues] = GLSP(X_trn,Y_trn,gt,ww,bb,k1,k2,dim)
% original author @Tomek
%  global and local structure preservation

% % ww balanced parameter between intra-class data
% % bb balanced parameter between inter-class data
% Make sure data is zero mean
X_trn_mean=mean(X_trn,1);
X_trn_Zero=bsxfun(@minus,X_trn,X_trn_mean);

% Make sure labels are nice
[classes,bar,Y_trn]=unique(Y_trn);
nc=length(classes);

% Intialize Sw
Sw=zeros(size(X_trn_Zero,2),size(X_trn_Zero,2));
% Compute total covariance matrix
St=cov(X_trn_Zero);
% Sum over classes

for i=1:nc
    cur_X=X_trn_Zero(Y_trn==i,:);
    
    %     Update within-class scatter
    C=cov(cur_X);
    p=size(cur_X,1)/(length(Y_trn)-1);
    Sw=Sw+(p*C);
end

% Compute between class scatter
Sb=St-Sw;

F1=zeros(size(X_trn,1),size(X_trn,1));
F2=zeros(size(X_trn,1),size(X_trn,1));
dist=L2_distance(X_trn',X_trn');
[tmp,index]=sort(dist,2);
for i=1:size(X_trn,1)
    temp=index(i,:);
    in1=find(Y_trn(temp)==Y_trn(i));
    in2=find(Y_trn(temp)~=Y_trn(i));
    F1(i,temp(in1(2:k1+1)))=1;
    F1(temp(in1(2:k1+1)),i)=1;
    F2(i,temp(in2(1:k2)))=1;
    F2(temp(in2(1:k2)),i)=1;
end

S1=diag(sum(F1));
S2=diag(sum(F2));

Slw=X_trn'*(S1-F1)*X_trn;
Slb=X_trn'*(S2-F2)*X_trn;
% p is a tuning parameter that controls the tradeoff between global similarity information
% and local similarity information
Stw=ww*Sw+(1-ww)*Slw;

Stb=bb*Sb+(1-bb)*Slb;

symMatrix=gt*Stb-(1-gt)*Stw;

symMatrix(isnan(symMatrix)) = 0;
[eigvectors,eigvalues]=eig(symMatrix+eye(size(symMatrix,1))*1.e-8);
[shu,order]=sort(diag(eigvalues),'descend');
eigvalues=shu;
eigvectors=eigvectors(:,order);
eigenvectorslast=eigvectors(:,1:dim);
mapping=eigenvectorslast;
