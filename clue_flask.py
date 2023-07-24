from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("./PromptCLUE-base-v1-5")
model = T5ForConditionalGeneration.from_pretrained("./PromptCLUE-base-v1-5")
import torch
# from transformers import AutoTokenizer
# 修改colab笔记本设置为gpu，推理更快
device = torch.device('cuda')
model.to(device)
def preprocess(text):
    return text.replace("\n", "_")
def postprocess(text):
    return text.replace("_", "\n")
def answer(text, sample=False, top_p=0.6):
    '''sample：是否抽样。生成任务，可以设置为True;
       top_p：0-1之间，生成的内容越多样、
    '''
    text = preprocess(text)
    encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=768, return_tensors="pt").to(device)
    if not sample: # 不进行采样

        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128, num_beams=4, length_penalty=0.6)

    else: # 采样（生成）
        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128, do_sample=True, top_p=top_p)


    out_text = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
    return postprocess(out_text[0])
if __name__ == '__main__':
    f = open("./prompt_bak.txt")
    lines = f.read()
    print(lines)
    pp = answer(lines)

    print("-----------输出结果-------------")
    print(pp)



