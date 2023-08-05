from statefun_tasks.context import TaskContext
from statefun_tasks.messages_pb2 import TaskResult, TupleOfAny
from statefun_tasks.serialisation import pack_any


class ResultEmitter(object):
    def __init__(self):
        pass

    def emit_result(self, context: TaskContext, task_request, task_result_or_exception):
        # the result of this task is the result of the pipeline
        if isinstance(task_result_or_exception, TaskResult):

            # if we are not a fruitful pipeline then zero out the result
            if not context.pipeline_state.is_fruitful:
                task_result_or_exception.result.CopyFrom(pack_any(TupleOfAny()))

            context.storage.task_result = task_result_or_exception
        else:
            # task failed or was cancelled
            context.storage.task_exception = task_result_or_exception

        # either send a message to egress if reply_topic was specified
        if task_request.HasField('reply_topic'):
            context.send_egress_message(topic=task_request.reply_topic, value=task_result_or_exception)

        # or call back to a particular flink function if reply_address was specified
        elif task_request.HasField('reply_address'):
            address, identifer = context.to_address_and_id(task_request.reply_address)
            context.send_message(address, identifer, task_result_or_exception)

        # or call back to our caller (if there is one)
        elif context.pipeline_state.caller_id is not None:
            if context.pipeline_state.caller_id != context.get_caller_id():  # don't call back to self
                context.send_message(context.pipeline_state.caller_address, context.pipeline_state.caller_id,
                                     task_result_or_exception)
