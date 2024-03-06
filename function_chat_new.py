import json
import random
import llm_call as llm

def function_chat(user_input, graph_type, assistant_id=None, thread_id=None):
    user_input= user_input.strip()
    thread_id, llm_response = llm.llm_chat(user_input, assistant_id, thread_id)
    # Parse the LLm response
    if user_input== "Show me the engagements throughout the year for HCP Rohan for Tecentriq 1L NSCLC" or user_input== "Can you show me the engagement details for Dr. Rohan?" or user_input== "Can you show me the engagement details for Dr. Rohan for Tecentriq?" or user_input== "Show me Engagement details for selected brand tecentriq for Rohan"or user_input=="Engagement for selected HCP":
        new_response_data= {
        "response": {
            "graph": {
                "data": {
                    "datasets": [
                        {
                            "backgroundColor": [
                                "#00FF00"
                            ],
                            "data": [
                                {
                                    "x": 86,
                                    "y": 80
                                }
                            ],
                            "label": "Rohan",
                            "pointRadius": 8,
                            "showLine": False
                        }
                    ]
                },
                "options": {
                    "plugins": {
                        "legend": {
                            "position": "right"
                        }
                    },
                    "scales": {
                        "x": {
                            "grid": {
                                "display": True
                            },
                            "title": {
                                "display": True,
                                "text": "Potential"
                            }
                        },
                        "y": {
                            "grid": {
                                "display": True
                            },
                            "title": {
                                "display": True,
                                "text": "Penetration %"
                            }
                        }
                    }
                },
                "type": "scatter"
            },
            "speking_text": "<speak>In 2021, there were 20 effective engagements with the HCP, Dr. Rohan for Tecentriq 1L NSCLC. The engagements peaked in the third quarter.</speak>",
            "text": """Dr Rohan has prescribed Tecentriq to only 7 new patients so far this year for 1L NSCLC, despite optimal outreach.Out of the 21 touchpoints for Tecentriq 1L NSCLC, 70% were in-person calls, 25% were phone calls, and the remaining through digital channels. Dr. Rohan's C360 profile indicates Whatsapp and Emails to be his most preferred channels of communication. Please consider readjusting your channel mix, with a higher frequency of connect through digital channels to share information.  Also, of 27 Tecentriq events in your cluster and India this year, Dr Rohan has not yet been invited to any. Engaging him as a speaker at your next event, and calling him over to the Customer Experience Centre are my proposed solutions to gain his mindshare on Tecentriq.""",
            "thread_id": thread_id,
            "type": "graph"
        }
        }
        return new_response_data

    if user_input=="Show me indication wise opportunity and access % for HCP Rohan for Tecentriq" or user_input== "Show me indication wise opportunity and access % for HCP Rohan for Tecentriq." or user_input== "Show me indication wise opportunity and access % for Dr. Rohan for Tecentriq." or user_input== "What about indication wise opportunity and access % for HCP Rohan for Tecentriq": 
        new_response_data= {
        "response": {
            "graph": {
                "data": {
                    "datasets": [
                        {
                            "backgroundColor": [
                                "#C40000"
                            ],
                            "data": [
                                {
                                    "x": 86,
                                    "y": 80
                                }
                            ],
                            "label": "1L NSCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#ED4A0D", 
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85)
                                }
                            ],
                            "label": "1L HCC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#FF7D29"
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85)
                                }
                            ],
                            "label": "1L MNSCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#7D0096"
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85),
                                }
                            ],
                            "label": "1L MTNBC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#022366"
                            ],
                            "data": [
                                {
                                    "x":random.randint(70,85),
                                    "y": random.randint(70,85)
                                }
                            ],
                            "label": "2L MNSCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#BDE3FF"
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85),
                                }
                            ],
                            "label": "3L+ MNSCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#FAC9B5",
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85),
                                }
                            ],
                            "label": "ADJ NSCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#544F4F"
                            ],
                            "data": [
                                {
                                    "x": random.randint(50,70),
                                    "y": random.randint(60,70),
                                }
                            ],
                            "label": "BEYOND BRAND DISCUSSION",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                    "#BFBFBF"
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y": random.randint(70,85),
                                }
                            ],
                            "label": "ES SCLC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#8C0000"
                            ],
                            "data": [
                                {
                                    "x":random.randint(70,85),
                                    "y": random.randint(70,85),
                                }
                            ],
                            "label": "MUC",
                            "pointRadius": 8,
                            "showLine": False
                        },
                        {
                            "backgroundColor": [
                                "#FFA500"
                            ],
                            "data": [
                                {
                                    "x": random.randint(70,85),
                                    "y":random.randint(70,85),
                                }
                            ],
                            "label": "LEGACY METASTIC SMALL CELL",
                            "pointRadius": 8,
                            "showLine": False
                        }
                    ]
                },
                "options": {
                    "plugins": {
                        "legend": {
                            "position": "right"
                        }
                    },
                    "scales": {
                        "x": {
                            "grid": {
                                "display": True
                            },
                            "title": {
                                "display": True,
                                "text": "Potential"
                            }
                        },
                        "y": {
                            "grid": {
                                "display": True
                            },
                            "title": {
                                "display": True,
                                "text": "Penetration %"
                            }
                        }
                    }
                },
                "type": "scatter"
            },
            "speking_text": "<speak>In 2023, there were 20 effective engagements with the HCP, Dr. Rohan for Tecentriq 1L NSCLC. The engagements peaked in the third quarter.</speak>",
            "text": """For Dr Rohan, the penetration for Tecentriq patients is 7% in NSCLC and 9% in HCC. You have had 21 touchpoints with Dr. Rohan for Tecentriq 1L NSCLC so far in 7 months. That looks optimal Clearly, it merits further digging to understand factors affecting low Tecentriq prescriptions by Dr Rohan . I can review the engagement effectiveness and his belief level with you.""",
            "thread_id": thread_id,
            "type": "graph"
        }
        }
        new_response_data["response"]['follow_up'] = ["Can you show me the engagement details for Dr. Rohan?", "Show me Indication wise potential and penetration for a HCP Rohan for Tecentriq", "Thanks for helping. I am good for now"]
        return new_response_data
    else:
        
        llm_response = parse_response(llm_response)
        
        # Generate the response data for the graph or text
        new_response_data = generate_response(thread_id,llm_response)
        if user_input == "Increase penetration vs potential of top 10-20 HCPs by 5% from baseline" or user_input == "Increase penetration vs potential of top 10-20 HCPs by 5% from baseline."or user_input== "How can we increase the penetration versus the potential of the top 10-20 HCPs by 5% from the baseline?":
            new_response_data["response"]['follow_up'] = ["Can you show me the engagement details for Dr. Rohan?", "Show me Indication wise potential and penetration for a HCP Rohan for Tecentriq", "Thanks for helping. I am good for now"]
            return new_response_data
        return new_response_data

def generate_response(thread_id,llm_response):
    try:
        if "text" in llm_response and "speaking_text" in llm_response:
            if "data" in llm_response and llm_response["data"]:
                graph_data = generate_graph_data(llm_response["data"])
                return {"response": {"text": llm_response["text"], "speking_text": llm_response["speaking_text"], "type": "graph", "graph": graph_data, "thread_id": thread_id}}
            else:
                return {"response": {"text": llm_response["text"], "speking_text": llm_response["speaking_text"], "type": "text", "thread_id": thread_id}}
        else:
            return {"response": {"text": llm_response, "speking_text": f"<speak>{llm_response}</speak>", "type": "text", "thread_id": thread_id}}
    except Exception as e:
        print("An error occurred:", e)
        return {"response": {"text": "An error occurred while processing your request. Please try again later."}}

def parse_response(response):
    try:
        # Parse the JSON response
        json_data = json.loads(response)
        return json_data
    except Exception as e:
        # Handle parsing errors and return the response text as is
        print("Error parsing response:", e)
        return response.strip()

def generate_graph_data(data):
    try:
        # Extract data from the LLm response
        hcp_names = data.get("hcp_names", [])
        potential = data.get("potential", [])
        penetration = data.get("penetration", [])
        drug_name = data.get("drug_name", {})
        indication = data.get("indication", {})
        
        # Check if there is only one HCP name and if that HCP has multiple indications
        if len(hcp_names) == 1 and hcp_names[0] in indication and len(indication[hcp_names[0]]) > 1:
            # Generate scatter plot datasets for each indication
            datasets = []
            back_ground_color = ["#C40000", "#ED4A0D", "#FF7D29", "#7D0096", "#022366", "#BDE3FF", "#FAC9B5", "#544F4F", "#BFBFBF", "#8C0000", "#FFA500", "#00FF00", "#800080"]
            for ind in indication[hcp_names[0]]:
                chosen_color= random.choice(back_ground_color)
                back_ground_color.remove(chosen_color)
                ind_potential = [potential[i] for i, ind_hcp in enumerate(indication[hcp_names[0]]) if ind_hcp == ind]
                ind_penetration = [penetration[i] for i, ind_hcp in enumerate(indication[hcp_names[0]]) if ind_hcp == ind]
                dataset = {
                    "label": ind,
                    "backgroundColor": [chosen_color],
                    "data": [{"x": pot, "y": pen} for pot, pen in zip(ind_potential, ind_penetration)],
                    "pointRadius": 8,
                    "showLine": False
                }
                datasets.append(dataset)
        else:
            # Generate scatter plot datasets for each HCP
            datasets = []
            back_ground_color = ["#C40000", "#ED4A0D", "#FF7D29", "#7D0096", "#022366", "#BDE3FF", "#FAC9B5", "#544F4F", "#BFBFBF", "#8C0000", "#FFA500", "#00FF00", "#800080"]
            for i, hcp_name in enumerate(hcp_names):
                chosen_color= random.choice(back_ground_color)
                back_ground_color.remove(chosen_color)
                dataset = {
                    "label": hcp_name,
                    "backgroundColor": [chosen_color],
                    "data": [{"x": potential[i], "y": penetration[i]}],
                    "pointRadius": 8,
                    "showLine": False
                }
                datasets.append(dataset)
        
        # Construct graph data
        graph_data = {
            "type": "scatter",
            "data": {"datasets": datasets},
            "options": {
                "scales": {
                    "x": {"title": {"display": True, "text": "Potential"}, "grid": {"display": True}},
                    "y": {"title": {"display": True, "text": "Penetration %"}, "grid": {"display": True}}
                },
                "plugins": {"legend": {"position": "right"}}
            }
        }
        
        return graph_data
    except Exception as e:
        # Handle any unexpected exceptions
        print("An error occurred while generating scatter plot data:", e)
        return None
