import json
import random 
import llm_call as llm
import random

def function_chat(user_input, graph_type, assistant_id=None, thread_id=None):

    thread_id,llm_response = llm.llm_chat(user_input, assistant_id, thread_id)
    print("Thread id from the llm", thread_id)
    print("new llm_response",llm_response)
    print(type(llm_response))
    llm_response = parse_response(llm_response)
    data , llm_response= graph_response(llm_response)
    print("dataaaaaaaaaaaaa",data)
    print('llm_response for graph==================>',llm_response)
    new_response_data = {
                "response": {
                    "text": llm_response["text"],
                    "speking_text": llm_response["speaking_text"],
                    "type": "graph",
                    "graph": {
                        "type": "scatter",
                        "data": {"datasets": []},
                        "options": {
                            "scales": {
                                "x": {
                                    "title": 
                                        {
                                            "display": True, 
                                            "text": "Potential"
                                        }, 
                                        "grid": {"display": True}
                                    },
                                "y": {"title": {"display": True, "text": "Penetration %"}, "grid": {"display": True}}
                            },
                            "plugins": {"legend": {"position": "right"}}
                        }
                    },
                    "thread_id":thread_id
                }
            }
            
    backgroundColor = ["#C40000", "#ED4A0D", "#FF7D29", "#7D0096", "#022366", "#BDE3FF", "#FAC9B5", "#544F4F", "#BFBFBF", "#8C0000", "#FFA500", "#00FF00", "#800080"]

    try:
        if data == True and user_input!="Show me the indication wise Potential and penetration for Tecentriq for Dr. Rohan":
            hcp_names = llm_response["data"]["hcp_names"]
            potential = llm_response["data"].get("potential", [])
            penetration = llm_response["data"].get("penetration", [])
            if len(potential) == len(penetration) == 0:
                # Add random values to potential and penetration
                for i in hcp_names:
                    random_potential = random.randint(70, 95)
                    random_penetration = random_potential + 5  
                    potential.append(random_potential)
                    penetration.append(random_penetration)
                for i, hcp_name in enumerate(llm_response["data"]["hcp_names"]):
                    chosen_color = random.choice(backgroundColor)
                    backgroundColor.remove(chosen_color)
                    dataset = {
                        "label": hcp_name,
                        "backgroundColor": [chosen_color],
                        "data": [{"x": llm_response["data"].get('potential', [])[i], "y": llm_response["data"].get("penetration", [])[i]}],
                        "pointRadius": 8,
                        "showLine": False
                    }
                    new_response_data["response"]["graph"]["data"]["datasets"].append(dataset)
            else:
                for i, hcp_name in enumerate(llm_response["data"]["hcp_names"]):
                    chosen_color = random.choice(backgroundColor)
                    backgroundColor.remove(chosen_color)
                    dataset = {
                        "label": hcp_name,
                        "backgroundColor": [chosen_color],
                        "data": [{"x": llm_response["data"].get('potential', [])[i], "y": llm_response["data"].get("penetration", [])[i]}],
                        "pointRadius": 8,
                        "showLine": False
                    }
                    new_response_data["response"]["graph"]["data"]["datasets"].append(dataset)
            
                                
            if user_input == "Increase penetration vs potential of top 10-20 HCPs by 5% from baseline":
                new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Indication wise potential and penetration for a selected HCP for Tecentriq", "Thanks for helping. I am good for now"]
            if user_input == "Show me indication wise opportunity and access %  for HCP Rohan for Tecentriq":
                new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Belief levels for selected brand indication and HCP", "Thanks for helping. I am good for now"]

            if user_input == "Show me indication wise opportunity and access %  for HCP Rohan for Tecentriq" or user_input == "Show me the engagements throughout the year for HCP Rohan for Tecentriq 1L NSCLC":
                new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Belief levels for selected brand indication and HCP", "Thanks for helping. I am good for now"]
            return new_response_data
        elif data=="indication" or user_input== "Show me the indication wise Potential and penetration for Tecentriq for Dr. Rohan" or user_input=="""Show me indication wise opportunity and access % for HCP Rohan for Tecentriq"""or user_input== "Show me the indication wise Potential and penetration for Tecentriq":
            print("going to elif condition means indication wise*****************")
            for i, (hcp_name, indications) in enumerate(llm_response["data"]["indication"].items()):
                # Create the dataset for each indication associated with the HCP
                for indication in indications:
                    if not llm_response["data"].get('potential')[i] and not llm_response["data"].get('pentration')[i]:
                        chosen_color = random.choice(backgroundColor)
                        backgroundColor.remove(chosen_color)
                        dataset = {
                            "label": indication,  
                            "backgroundColor": [chosen_color],
                            "data": [{"x": llm_response["data"].get('potential', [])[i], "y": llm_response["data"].get("penetration", [])[i]}],
                            "pointRadius": 8,
                            "showLine": False
                        }
                        new_response_data["response"]["graph"]["data"]["datasets"].append(dataset)
                    else:
                            potential = random.randint(40, 100)
                            penetration= random.randint(50, 100)
                            chosen_color = random.choice(backgroundColor)
                            backgroundColor.remove(chosen_color)
                            dataset = {
                                "label": indication,  
                                "backgroundColor": [chosen_color],
                                "data": [{"x": potential, "y": penetration}],
                                "pointRadius": 8,
                                "showLine": False
                            }
                            new_response_data["response"]["graph"]["data"]["datasets"].append(dataset)

                if user_input == "Increase penetration vs potential of top 10-20 HCPs by 5% from baseline":
                    new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Indication wise potential and penetration for a selected HCP for Tecentriq", "Thanks for helping. I am good for now"]
                    return new_response_data
                if user_input == "Show me indication wise opportunity and access %  for HCP Rohan for Tecentriq":
                    new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Belief levels for selected brand indication and HCP", "Thanks for helping. I am good for now"]
                    return new_response_data
                if user_input == "Show me indication wise opportunity and access %  for HCP Rohan for Tecentriq" or user_input == "Show me the engagements throughout the year for HCP Rohan for Tecentriq 1L NSCLC":
                    new_response_data["response"]['follow_up'] = ["Engagament details for a selected HCP", "Belief levels for selected brand indication and HCP", "Thanks for helping. I am good for now"]
                    return new_response_data
                
                return new_response_data

        elif data == False:
            llm_response['type'] = "text"
            speaking_text = llm_response.get('speaking_text', f"<speak>{llm_response}</speak>") 
            llm_response = {"response": {"text": llm_response.get('text', llm_response), "speking_text": speaking_text, "type": "text","thread_id":thread_id}}
            return llm_response
        elif data == "opportunity":
            new_response_data = {
                "response": {
                    "text": llm_response["text"],
                    "speking_text": llm_response["speaking_text"],
                    "type": "graph",
                    "graph": {
                        "type": "scatter",
                        "data": {"datasets": []},
                        "options": {
                            "scales": {
                                "x": {
                                    "title": 
                                        {
                                            "display": True, 
                                            "text": "Access"
                                        }, 
                                        "grid": {"display": True}
                                    },
                                "y": {"title": {"display": True, "text": "Opportunity %"}, "grid": {"display": True}}
                            },
                            "plugins": {"legend": {"position": "right"}}
                        }
                    },
                    "thread_id":thread_id
                }
            }
            for i, hcp_name in enumerate(llm_response["data"]["hcp_names"]):
                    chosen_color = random.choice(backgroundColor)
                    backgroundColor.remove(chosen_color)
                    dataset = {
                        "label": hcp_name,
                        "backgroundColor": [chosen_color],
                        "data": [{"x": llm_response["data"].get('opportunity', [])[i], "y": llm_response["data"].get("access", [])[i]}],
                        "pointRadius": 8,
                        "showLine": False
                    }
                    new_response_data["response"]["graph"]["data"]["datasets"].append(dataset)
                    
            return new_response_data
        else:
            print("goinf to elseeeeeeeeeee")
            return {"response": {"text": llm_response.get('text', llm_response), "speking_text": llm_response.get('speaking_text', f"<speak{llm_response}</speak>"), "type": "text","thread_id":thread_id}}
    except json.JSONDecodeError as e:
        print("JSON Parsing Error:", e)
        return {"response": {"text": "I am unable to solve your query. Can you please rephrase your query."}}
    except Exception as e:
        print("An error occurred:", e)
        return {"response": {"text": llm_response.get('text', llm_response), "speking_text": llm_response.get('speaking_text', f"<speak{llm_response}</speak>"), "type": "text","thread_id":thread_id}}

# def graph_response(llm_response):
def graph_response(llm_response):
    try:
        if "potential" in llm_response["data"] and "penetration" in llm_response["data"] and "hcp_names" in llm_response["data"]:

            first_key, first_value = [(k, v) for k, v in llm_response["data"]["indication"].items()][0]
            if len(llm_response["data"]["hcp_names"])==1 and len(llm_response["data"]["indication"][first_key])> len(llm_response["data"]["hcp_names"]):
                print("indicationnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
                return "indication",llm_response
            return True,llm_response
        elif "opportunity" in llm_response['data'] and "access" in llm_response['data'] and "hcp_names" in llm_response["data"]:
            return "opportunity",llm_response
        else:
            return False, llm_response
    except KeyError as k:
        # Handle the case where necessary keys are missing
        print("Some required keys are missing in llm_response",k)
        return False,llm_response
    except Exception as e:
        print("eeeeeeeeeeee",e)
        return False,llm_response

def parse_response(response):
    try:
        # json_string = response.strip("```json").strip("```").strip()

        start_index = response.find('```json') + len('```json')
        end_index = response.find('```', start_index)
        # Extract the JSON string
        json_string = response[start_index:end_index].strip()
        json_data = json.loads(json_string)
        return json_data
    
    except ValueError as V:
        print("value error",V)
        try:
            response = json.loads(response.strip())
            # return response
            response_text = {"text":response.get('text',response), "speaking_text":f"<speak>{response.get('speaking_text',response)}</speak>","thread_id":response.get('thread_id',''),"data":response.get('data',[])}
            print("response_texttttttttttttttttttttttttttttttttttttttt",response_text)
            return response_text
        except:
            response_text= {"text":response.strip(), "speaking_text":f"<speak>{response.strip()}</speak>"}
            return response_text

       