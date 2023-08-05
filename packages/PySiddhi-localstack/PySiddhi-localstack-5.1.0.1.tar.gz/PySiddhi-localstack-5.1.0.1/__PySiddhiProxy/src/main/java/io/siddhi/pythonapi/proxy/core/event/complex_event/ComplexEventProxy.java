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

package io.siddhi.pythonapi.proxy.core.event.complex_event;

import io.siddhi.core.event.ComplexEvent;
import io.siddhi.pythonapi.DataWrapProxy;

/**
 * Proxy on io.siddhi.core.event.ComplexEvent
 */
public class ComplexEventProxy {
    public DataWrapProxy[] getOutputData(ComplexEvent target) {
        return DataWrapProxy.wrapArray(target.getOutputData());
    }

    public void setOutputData(ComplexEvent target, DataWrapProxy data, int index) {
        target.setOutputData(data.getData(), index);
    }
}
