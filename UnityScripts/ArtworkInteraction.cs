using UnityEngine;

/// <summary>
/// Controller for artwork interactions in the virtual museum
/// Handles emotion button presses and delegates to EmotionSender
/// </summary>
public class ArtworkInteraction : MonoBehaviour
{
    [Header("Artwork Configuration")]
    [Tooltip("Unique ID of this artwork in the backend database")]
    public int obraId;

    [Header("References")]
    [Tooltip("Component responsible for sending emotion data to backend")]
    public EmotionSender sender;

    /// <summary>
    /// Called when user selects an emotion for this artwork
    /// </summary>
    /// <param name="estado">The selected emotion state (e.g., "triste", "feliz")</param>
    public void OnUserEmotionSelected(string estado)
    {
        if (sender != null)
        {
            sender.SendEmotion(estado, obraId);
        }
        else
        {
            Debug.LogError("EmotionSender not assigned to ArtworkInteraction!");
        }
    }
}