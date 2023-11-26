namespace ConsoleApp;

public class TextReplacer
{
    // کالکشن خود را در این قسمت تعریف کنید

    public string tagChar;
    private Dictionary<string, string> tagReplacements;
    public TextReplacer(string tagChar)
    {
        this.tagChar = tagChar;
        tagReplacements = new Dictionary<string, string>();
    }

    public void AddTag(string tagName, string tagValue)
    {
        tagReplacements.Add(tagChar + tagName, tagValue);
        // تگ را به کالکشن خود اضافه کنید
    }

    public string ReplaceTags(string text)
    {
        foreach (var (tagName, value) in tagReplacements)
        {
            text = text.Replace(tagName, value);
        }
        return text;
    }
}
