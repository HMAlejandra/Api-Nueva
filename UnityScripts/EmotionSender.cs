using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using TMPro; // For TextMeshPro, if using TMP

/// <summary>
/// Handles communication with the backend API for emotion-based artwork comments
/// Sends emotion and artwork ID, receives and displays AI-generated comment
/// </summary>
public class EmotionSender : MonoBehaviour
{
    [Header("API Configuration")]
    [Tooltip("Backend API base URL")]
    public string apiBaseUrl = "http://localhost:8000"; // Adjust for your backend URL

    [Header("UI References")]
    [Tooltip("Text component to display the AI comment")]
    public TextMeshProUGUI commentDisplayText; // Or use UnityEngine.UI.Text if not using TMP

    [Header("Debug")]
    [Tooltip("Log API responses for debugging")]
    public bool debugMode = true;

    private const string ENDPOINT = "/api/obra/emocion";

    /// <summary>
    /// Sends emotion data to backend and handles response
    /// </summary>
    /// <param name="estadoAnimo">User's emotional state</param>
    /// <param name="obraId">Artwork ID</param>
    public void SendEmotion(string estadoAnimo, int obraId)
    {
        if (debugMode)
        {
            Debug.Log($"Sending emotion: {estadoAnimo} for artwork ID: {obraId}");
        }

        StartCoroutine(SendEmotionRequest(estadoAnimo, obraId));
    }

    private IEnumerator SendEmotionRequest(string estadoAnimo, int obraId)
    {
        // Create JSON payload
        EmotionRequest requestData = new EmotionRequest
        {
            estado_animo = estadoAnimo,
            obra_id = obraId
        };

        string jsonPayload = JsonUtility.ToJson(requestData);

        if (debugMode)
        {
            Debug.Log($"JSON Payload: {jsonPayload}");
        }

        // Create web request
        string url = apiBaseUrl + ENDPOINT;
        UnityWebRequest request = new UnityWebRequest(url, "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonPayload);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        // Send request
        yield return request.SendWebRequest();

        // Handle response
        if (request.result == UnityWebRequest.Result.Success)
        {
            string responseText = request.downloadHandler.text;

            if (debugMode)
            {
                Debug.Log($"Response: {responseText}");
            }

            try
            {
                EmotionResponse response = JsonUtility.FromJson<EmotionResponse>(responseText);

                if (debugMode)
                {
                    Debug.Log($"Parsed comment: {response.comentario}");
                }

                // Display the comment
                DisplayComment(response.comentario);
            }
            catch (System.Exception e)
            {
                Debug.LogError($"Error parsing response: {e.Message}");
                DisplayComment("Error al procesar la respuesta del servidor.");
            }
        }
        else
        {
            Debug.LogError($"API Error: {request.error}");
            DisplayComment("Error de conexión con el servidor.");
        }
    }

    private void DisplayComment(string comment)
    {
        if (commentDisplayText != null)
        {
            commentDisplayText.text = comment;
        }
        else
        {
            Debug.Log($"AI Comment: {comment}");
        }
    }

    // Data classes for JSON serialization
    [System.Serializable]
    private class EmotionRequest
    {
        public string estado_animo;
        public int obra_id;
    }

    [System.Serializable]
    private class EmotionResponse
    {
        public int obra_id;
        public string comentario;
    }
}