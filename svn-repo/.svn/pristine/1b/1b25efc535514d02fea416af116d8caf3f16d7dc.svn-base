using System;
using System.Collections;
using System.Globalization;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class OtherTest
{
    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator ThisTestShouldFail()
    {
        Debug.Log("Test start:" + DateTime.Now.ToString(CultureInfo.InvariantCulture));
        var testObject = new GameObject();
        testObject.AddComponent<Scripts.PlayerController>();

        var playerController = testObject.GetComponent<Scripts.PlayerController>();
        playerController.DoSomething();
        
        // Use the Assert class to test conditions.
        // Use yield to skip a frame.
        yield return null;

        var position = testObject.transform.position;
        Debug.Log("Position: " + position.ToString());
        Assert.Greater(position.y, 9);
        
        Debug.Log("Note: the second part should fail!");
        Assert.Greater(position.x, 99);      
        
        
    }
}
