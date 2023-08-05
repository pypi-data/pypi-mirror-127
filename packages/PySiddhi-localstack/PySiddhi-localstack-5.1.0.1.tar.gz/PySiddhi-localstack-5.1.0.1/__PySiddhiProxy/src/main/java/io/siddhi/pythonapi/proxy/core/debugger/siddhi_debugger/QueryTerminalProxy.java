/*
 * Copyright (c) 2017, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
 *
 * WSO2 Inc. licenses this file to you under the Apache License,
 * Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package io.siddhi.pythonapi.proxy.core.debugger.siddhi_debugger;

import io.siddhi.core.debugger.SiddhiDebugger;

/**
 * Proxy on io.siddhi.core.debugger.SiddhiDebugger.QueryTerminal
 */
public class QueryTerminalProxy {
    public SiddhiDebugger.QueryTerminal IN() {
        return SiddhiDebugger.QueryTerminal.IN;
    }

    public SiddhiDebugger.QueryTerminal OUT() {
        return SiddhiDebugger.QueryTerminal.OUT;
    }

    private SiddhiDebugger.QueryTerminal enclosedValue = SiddhiDebugger.QueryTerminal.IN;

    public QueryTerminalProxy() {
        //Constructor let open to allow access of IN and OUT methods from Python (because Pyjnius doesn't support
        // class level methods)
    }

    public QueryTerminalProxy(SiddhiDebugger.QueryTerminal enclosedValue) {
        this.enclosedValue = enclosedValue;
    }

    public SiddhiDebugger.QueryTerminal getValue() {
        return this.enclosedValue;
    }

    public boolean isValueIn() {
        return this.enclosedValue == IN();
    }

    public boolean isValueOut() {
        return this.enclosedValue == OUT();
    }
}
