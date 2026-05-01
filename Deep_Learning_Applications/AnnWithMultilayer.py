# -------------------------------------------------------------------------------------------------------
#  Network Structure : 
#        Input Layer : 2 input 
#        Hidden Layer : 2 neurons with ReLU activation 
#        Output Layer : 1 neuron with Sigmoid activation
#
#  Purpose : 
#       To understand how data moves from input layer 
#       to hidden layer and finally to output layer.
# -------------------------------------------------------------------------------------------------------

import math


# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_ReLU
# Description   : Applies ReLU activation function 
# Formula       : ReLU(x) = max(0,x)
# Use           : Commonly used in hidden layers 
# ------------------------------------------------------------------------------------------------------

def Marvellous_ReLU(value):
    return max(0,value)

# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Sigmoid
# Description   : Applies Sigmoid activation function 
# Formula       : 1 / (1 + e ^(-x))
# Use           : Commonly used in Output  layer for binary classification 
# Output range  : 0 to 1 
# ------------------------------------------------------------------------------------------------------

def Marvellous_Sigmoid(value):
    return 1/(1 + math.exp(-value))

# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Calculate_Weight_Sum
# Description   : Calculate weight sum of inputs
# Formula       : z = (x1 *w1 + x2 * w2 + ..... xn*wn) b+
# Parameters    : 
#     Inputs -> List of input values 
#     weights -> List of weights
#     bias    -> Bias value
# 
# Returns       : Weighted sum 
# ------------------------------------------------------------------------------------------------------

def Marvellous_Calculate_Weight_Sum(inputs,weights,bias):
    weighted_sum = sum(weights*inputs for weights , inputs in zip(weights,inputs))+ bias
    return weighted_sum

# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Display_Multiplication_Detail
# Description   : Display Step by step multiplication of inputs
#                 and weights for one neuron 
# Parameters    : 
#     Inputs -> List of input values 
#     weights -> List of weights
# ------------------------------------------------------------------------------------------------------

def Marvellous_Display_Multiplication_Detail(inputs, weights):
    print("Strep 1 : Multiply inputs by corresponding weights")
    for index in range(len(inputs)):
        print(f"({weights[index]} * {inputs[index]}) = {weights[index] * inputs[index]:.3f}")
        


# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Process_Hidden_Layer
# Description   : Process all neurons of hidden layer 
#                 using ReLU activation function 
#                 and weights for one neuron 
# Parameters    : 
#     Inputs -> Input values from input layer
#     hidden_weights -> weights matrix for hidden layer 
#     hidden_biases   -> Bias list for hidden neurons
# Returns       : List of hidden layer outputs
# ------------------------------------------------------------------------------------------------------

def Marvellous_Process_Hidden_Layer(inputs, hidden_weights,hidden_biases):
    hidden_outputs  =[]
    print("\n======================================= HIDDEN LAYER ========================================")
    
    for neuron_index in range(len(hidden_weights)):
        print(f"Hidden Neuron {neuron_index + 1} :")
        
        current_weights = hidden_weights[neuron_index]
        current_bias = hidden_biases[neuron_index]
        
        # Display multiplication details 
        Marvellous_Display_Multiplication_Detail(inputs,current_weights)
        
        # calculate weighted sum 
        
        z_value = Marvellous_Calculate_Weight_Sum(inputs,current_weights,current_bias)
        print(f"Step 2 : Add all multiplication results and bias {current_bias}")
        print(f"z = {z_value:.3f}")
        
        # Apply ReLU Activation 
        
        activate_output = Marvellous_ReLU(z_value)
        print(f"Step 3 : Apply ReLU activation ")
        print(f"ReLU({z_value:.3f}) = {activate_output:.3f}\n")
        
        hidden_outputs.append(activate_output)
    return hidden_outputs


# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Process_Output_Layer
# Description   : Process Output layer neuron using
#                 Sigmoid activation function
# Parameters    : 
#     hidden_outputs -> Outputs from hidden layer
#     output_weights -> weights of output neuron
#     output_bias    -> Bias of output neuron
# Returns       : Final weighted sum and final output 
# ------------------------------------------------------------------------------------------------------

def Marvellous_Process_Output_Layer(hidden_outputs,output_weights,output_bias):
    print("\n================================ OUTPUT LAYER ================================")
    print("Output Neuron : ")
    print("Step 1 : Multiply hidden layer outputs by output weights") 
    for index in range(len(hidden_outputs)):
        print(f"({output_weights[index]} * {hidden_outputs[index]:.3f}) = "
              f"{output_weights[index] * hidden_outputs[index]:.3f}"
              )
    
    # Calculate weighted sum for output layer 
    z_output = Marvellous_Calculate_Weight_Sum(hidden_outputs,output_weights,output_bias)
    print(f'Step 2 : Add all multiplication result and bias {output_bias}')
    print(f"z= {z_output:.3f}")
    # Apply Sigmoid activation 
    final_output = Marvellous_Sigmoid(z_output) 
    print("Step 3 : Apply Sigmoid activation ")
    print(f"Sigmoid ({z_output:.3f}) = {final_output:.3f}")
    
    return    z_output,final_output


# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_Display_Network_Summary
# Description   : Display final outputs of network 
# Parameters    : 
#     hidden_outputs -> hidden layer output 
#     final_output -> Output layer final value 
# ------------------------------------------------------------------------------------------------------

def Marvellous_Display_Network_Summary(hidden_output, final_output):
    print("\n====================== FINAL SUMMARY =============================")
    print(f"Hidden Network output : {hidden_output}")
    print(f"Final Network Output : {final_output :.3f}")
    print(f"Confidence Percentage : {final_output * 100:.2f}%")
    
    if final_output >= 0.5:
        print("Prediction     :  Positive class ")
    else:
        print("Prediction     :  Negative  class ")





# ------------------------------------------------------------------------------------------------------
# Function Name : Marvellous_ANN_Forward_Pass
# Description   :Complete forward pass of ANN
# Parameters    : 
#     inputs  -> List of inputs values 
# Flow 
#     Input Layer -> Hidden Layer  -> Output Layer  
# ------------------------------------------------------------------------------------------------------

def Marvellous_ANN_Forward_Pass(inputs):
    print("\n============================ INPUT LAYER ====================================\n")
    print(f"Input x1 = {inputs[0]}")
    print(f"Input x2 = {inputs[1]}")
    
    #--------------------------------------------------
    # Hidden layer weights and biases 
    #  Two neurons in hidden layer 
    #-------------------------------------------------- 
    hidden_weights = [
        [0.5,-0.2], # Weight for hidden neuron 1
        [0.8,0.4]   # Weights for hidden neuron 2
    ]
    
    hidden_biases = [
        0.1, # bias for hidden neurons 1
        -0.1 # Bias for hidden neuron 2
    ]
    #------------------------------------------------------------------------
    # output layer weights an dbas 
    # One neuron in output layer 
    #------------------------------------------------------------------------   
    
    output_weights = [1.0 , -1.5]
    output_bias = 0.2
    
    # Process Hidden layer 
    
    hidden_output = Marvellous_Process_Hidden_Layer(
        inputs,
        hidden_weights,
        hidden_biases
    )
    # Process Output layer 
    z_output , final_output  = Marvellous_Process_Output_Layer(
        hidden_output,
        output_weights,
        output_bias
    )
    
    # Display Summary 
    
    Marvellous_Display_Network_Summary(hidden_output, final_output)

# ---------------------------------------------------
# Function Name : main 
# Description : Entery point of program 
# ----------------------------------------------------

def main():
    # Explain input values 
    inputs =[2.0,3.0]
    # Start Ann forward pass
    Marvellous_ANN_Forward_Pass(inputs)
    


if __name__ == "__main__":
    main()
