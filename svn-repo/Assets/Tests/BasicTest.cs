using System;
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class BasicTest
{
    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator BasicTestWithEnumeratorPasses()
    {
        Debug.Log("Test start:" + DateTime.Now.ToString());
        var testObject = new GameObject();
        testObject.AddComponent<Scripts.PlayerController>();
        
        // Use the Assert class to test conditions.
        // Use yield to skip a frame.
        yield return new WaitForSeconds(1);
        
        Debug.Log("Position: " + testObject.transform.position.ToString());
        Assert.Greater(testObject.transform.position.x, 0);      
    }
}
