
import requests
import os
import easyfed
import torch
def get_status(host,key,type,modeltype):
    req=reuqest(host,'get_status',data={'key':key,'type':type,'modeltype':modeltype})
    return req
def send_model(host,key,type,modeltype,model,loss=None):
    print('send_model',host,type)
    save_path=os.path.join(easyfed.client_dir,key)
    weight=model.state_dict()
    torch.save(weight, save_path)
    model = open(save_path, 'rb')
    file = {'file':model}
    req=reuqest(host,'send_model',data={'key':key,'type':type,'modeltype':modeltype,'acc':0,'loss':loss},file=file)

def download_model(host,modelurl,key):
    r=requests.get('%s%s'%(host,modelurl))
    print('downloading agg model from server .......')
    save_path=os.path.join(easyfed.client_dir,key)
    with open(save_path,"wb") as f:
        f.write(r.content)
    return save_path

def client_login(host,clientName,modeltype):
    result={} 
    result['result']=0
    cidfile=os.path.join(easyfed.client_dir,'.%s%scid.p'%(clientName,modeltype))
    if os.path.exists(cidfile):
        with open(cidfile,'r') as f:
            line=f.readline()
        if line:
            req=reuqest(host,'client_login',data={'clientName':clientName,'key':line.strip(),'modeltype':modeltype})
            result['result']=req['result']
            result['key']=line.strip()
    else:
        req=reuqest(host,'client_login',data={'clientName':clientName,'key':'','modeltype':modeltype})
        if req['key']:
             result['key']=req['key']
             with open(cidfile,'w') as f:
                 f.write(req['key'])
    return result
def reuqest(server_addres,controler,data,file=None):
    req = requests.post(url='%s/%s'%(server_addres,controler),data=data, files=file)
    return req.json()