'''
Placeholder app for Fattails.io
'''

import streamlit as st 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.figure_factory as ff


def main(): 
    st.title("FatTails.io")

    page = st.sidebar.selectbox("Select a page", ["Home", "Distributions", "Correlation"])

    if page == "Home":
        #st.subheader("Home")
        st.markdown("## Welcome!" )
        
        st.markdown("The primary goal of this site is to serve as an educational tool to help people build their statistical intuition \
        and help make sense of the technical companion of Taleb's  ** *Incerto* ** by providing interactive plots.")

        st.markdown("**Statistical Consequences of Fat Tails: Real World Preasymptotics, Epistemology, and Applications**: <https://arxiv.org/abs/2001.10488>")    

        st.markdown("**Disclaimer:** This site is not affiliated with N.N. Taleb - just big fans.")
        st.markdown("**Find an error? Have a suggestion?**" )  
        st.markdown("Let me know: <ian.hensel@fattails.io> , <https://twitter.com/IanHensel>")
        st.markdown("Contribute: <https://github.com/Cattleman/fattails>")

    if page == "Distributions":
        st.subheader("Distributions")

        st.markdown("Section is - WIP")

        st.markdown("### Thick Tailed")

        #st.text("Normal Distribution can be described by two values, the mean and standard deviation")

        st.markdown("### Subexponential")

        st.markdown("### Powerlaw") 

        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ["Group 1", "Group 2", "Group 3"]

        # Create distplot with custom bin_size
        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

        # Plot!
        st.plotly_chart(fig)


    elif page == "Random Walk":
        st.subheader("Random Walk")
        
        st.markdown("### Lets Take a walk")


    elif page == "Correlation":

        st.markdown("## Correlation - WIP")

        st.markdown("**Fooled by Correlation and Common Misinterpretations in Social 'Science' NNT - 2019**")

        st.markdown("### Resources:")
        st.markdown("**Stats 101 BS on Correlation:** <https://twitter.com/nntaleb/status/1113566110367002624>")
        st.markdown("**Entropy Methods vs Correlation:** <https://twitter.com/nntaleb/status/1111966227503689728>")
        st.markdown("**Mutual Information is Additive:** <https://twitter.com/nntaleb/status/1110552284730003463>")
        st.markdown("**Video:** <https://www.youtube.com/watch?v=p76bQlnVuBM>")
        st.markdown("**Paper:** <https://www.dropbox.com/s/18pjy7gmz0hl6q7/Correlation.pdf?dl=0> ")
    

        st.markdown("### The Point")

        st.markdown("The take-away: correlation cannot be used for non-random subsamples (Rule 1)")
        st.markdown("WIP (Rule 2)")
        st.markdown("WIP (Rule 3)")
        st.markdown("WIP (Rule 4)")

        # Set seed
        np.random.seed(42)

        # X,Y be normalized RV 

        # 1000 random integers between 0 and 50
        x = np.arange(start=-4,stop=4, step=8/1000) 

        # Positive Correlation with some noise
        y = x + np.random.normal(0,1.2, 1000)

        data = np.column_stack((x,y))
        plt.scatter(data[:,0],data[:,1])
        plt.plot(data[:,0],data[:,0], color='black', linewidth=2, linestyle="--")

        # Let's put it into a df to make masking easy!

        data = pd.DataFrame(data, columns=['x', 'y'])

        Q1 = data[(data['x'] >= 0) & (data['y'] >=0)]
        Q2 = data[(data['x'] > 0) & (data['y'] < 0)]
        Q3 = data[(data['x'] < 0) & (data['y'] < 0)]
        Q4 = data[(data['x'] < 0) & (data['y'] > 0)]

        # Get corr coef.
        overall_corr = np.round(data.corr().iloc[0][1],2)
        q1_corr = np.round(Q1.corr().iloc[0][1], 2) 
        q2_corr = np.round(Q2.corr().iloc[0][1], 2) 
        q3_corr = np.round(Q3.corr().iloc[0][1], 2) 
        q4_corr = np.round(Q4.corr().iloc[0][1], 2) 

        plt.title(f'Correlation by Quadrent \n Overall Corr: {overall_corr}', fontsize=16)
        plt.scatter(Q1['x'],Q1['y'], label='Q1')
        plt.scatter(Q2['x'],Q2['y'], label='Q2')
        plt.scatter(Q3['x'],Q3['y'], label='Q3')
        plt.scatter(Q4['x'],Q4['y'], label='Q4')
        #horizontal line
        plt.hlines(y=0,xmin=data['x'].min(), xmax=data['x'].max(), linestyles='--', alpha=0.5)
        # vertical line
        plt.vlines(x=0, ymin=data['y'].min(), ymax=data['y'].max(), linestyles='--', alpha=0.5)
        plt.text(2, 6, q1_corr)
        plt.text(-2, 4, q2_corr)
        plt.text(-2.2, -5.5, q3_corr)
        plt.text(2, -3, q4_corr)
        plt.legend()
        st.pyplot()


if __name__ == '__main__':
    main()    
