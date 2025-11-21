using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Button component for emotion selection
/// Assigns emotion state and calls ArtworkInteraction when clicked
/// </summary>
public class EmotionUIButton : MonoBehaviour
{
    [Header("Emotion Configuration")]
    [Tooltip("The emotion state this button represents")]
    public string emotionState = "feliz"; // e.g., "triste", "feliz", "ansiosa", "estresada"

    [Header("References")]
    [Tooltip("Reference to the ArtworkInteraction component on the parent artwork")]
    public ArtworkInteraction artworkInteraction;

    private Button button;

    private void Awake()
    {
        button = GetComponent<Button>();
        if (button != null)
        {
            button.onClick.AddListener(OnEmotionButtonClicked);
        }
    }

    private void OnEmotionButtonClicked()
    {
        if (artworkInteraction != null)
        {
            artworkInteraction.OnUserEmotionSelected(emotionState);
        }
        else
        {
            Debug.LogError("ArtworkInteraction not assigned to EmotionUIButton!");
        }
    }

    private void OnDestroy()
    {
        if (button != null)
        {
            button.onClick.RemoveListener(OnEmotionButtonClicked);
        }
    }
}