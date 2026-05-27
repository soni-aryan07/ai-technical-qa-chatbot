import json
from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

ANALYTICS_FILE = Path("analytics.json")

def load_analytics():

    if not ANALYTICS_FILE.exists():
        return []
    if ANALYTICS_FILE.stat().st_size == 0:
        return []
    
    with open(ANALYTICS_FILE, 'r') as file:
        return json.load(file)
    
def save_interaction(
        provider,
        model,
        question,
        answer,
        response_time,
        success=True,
        error=None
):
    data = load_analytics()

    interaction = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "provider": provider,
        "model": model,
        "question": question,
        "answer": answer,
        "response_time": response_time,
        "success": success,
        "error": error
    }

    data.append(interaction)

    with open(ANALYTICS_FILE, 'w') as file:
        json.dump(data, file, indent=4)



def get_dataframe():
    '''Converts analytics json into pandas dataframe'''

    data = load_analytics()

    if not data:
        return pd.DataFrame(columns=[
            'timestamp',
            'provider',
            'model',
            'question',
            'answer',
            'response_time',
            'success',
            'error'
        ])
    
    df = pd.DataFrame(data)

    return df

def get_summary():
    '''Creates a simple analytics summary'''
    
    df = get_dataframe()

    if df.empty:
        return 'No analytics yet'
    
    total_interactions = len(df)
    successful_requests = df['success'].sum()
    success_rate = successful_requests / total_interactions * 100
    avg_response_time = df['response_time'].mean()

    most_used_provider = df['provider'].mode()[0]
    most_used_model = df['model'].mode()[0]

    summary = f"""
# Analytics Summary

#### Total interactions: {total_interactions}
#### Successful Requests: {successful_requests}
#### Success Rate: {success_rate:.2f}%
#### Average Response Time: {avg_response_time:.2f}
#### Most Used Provider: {most_used_provider}
#### Most Used Model: {most_used_model}
"""
    
    return summary

def provider_usage_chart():
    '''Creates a bar chart showing how many times each provider was used'''

    df = get_dataframe()

    if df.empty:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, 'No data yet', ha='center', va='center', fontsize=14, color='gray')
        ax.axis('off')
        plt.close(fig)
        return fig
    
    provider_counts = df['provider'].value_counts()    

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

    fig, ax = plt.subplots(figsize=(10, 5))
    provider_counts.plot(kind='bar',color=colors, ax=ax)

    ax.set_title('Provider Usage')
    ax.set_xlabel('Provider')
    ax.set_ylabel('Number of requests')

    plt.xticks(rotation=0, fontsize=12)  # ensures labels are horizontal and readable
    plt.tight_layout()
    plt.close(fig)

    return fig

def response_time_chart():
    '''Create a line plot which shows response time over interactions'''

    df = get_dataframe()

    if df.empty:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, 'No data yet', ha='center', va='center', fontsize=14, color='gray')
        ax.axis('off')
        plt.close(fig)
        return fig
    
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df.index, df['response_time'], color='#4ECDC4', linestyle='--', marker= 'o')

    ax.set_title('Reponse Time Over Requests')
    ax.set_xlabel('Request Number')
    ax.set_ylabel('Response Time Seconds')

    plt.xticks(rotation=0, fontsize=12)  # ensures labels are horizontal and readable
    plt.tight_layout()
    plt.close(fig) #p prevents memory leak
    return fig