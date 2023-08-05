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

package io.siddhi.pythonapi.proxy.core.query.output.callback.query_callback;

import org.apache.log4j.Logger;
import io.siddhi.core.event.Event;
import io.siddhi.core.query.output.callback.QueryCallback;
import io.siddhi.pythonapi.threadfix.PyThreadFixCaller;

/**
 * Proxy class on io.siddhi.core.query.output.callback.QueryCallback
 */
public class QueryCallbackProxy extends QueryCallback {
    private ReceiveCallbackProxy receiveCallback = null;

    public void setReceiveCallback(ReceiveCallbackProxy value) {
        this.receiveCallback = value;
    }

    private static final Logger log = Logger.getLogger(QueryCallbackProxy.class);

    public void receive(long timestamp, Event[] inEvents, Event[] ouEvents) {
        PyThreadFixCaller.fix();

        if (this.receiveCallback != null)
            this.receiveCallback.receive(timestamp, inEvents, ouEvents);

    }

    @Override
    public void finalize() throws java.lang.Throwable {
        //We need to inform Python when Java GC collects so it can remove the references held
        log.info("Java GC Collection");
        this.receiveCallback.gc();
    }
}
